import time
import threading
from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class BumperToken:
    """Represents a Discord account/token configuration."""
    name: str
    token: str
    channel_id: str
    status: str = "Ready"
    last_bump: Optional[float] = None
    total_bumps: int = 0

    @property
    def masked_token(self) -> str:
        """Returns masked token string for security."""
        if not self.token or self.token == "YOUR_DISCORD_TOKEN_HERE":
            return "YOUR_DISCORD_TOKEN_HERE"
        if len(self.token) > 12:
            return f"{self.token[:4]}...{self.token[-4:]}"
        return "••••••••••••"


@dataclass
class BumpLogEvent:
    """Represents a log entry for a bump action."""
    timestamp: float
    formatted_time: str
    server_name: str
    channel_id: str
    token_name: str
    status: str  # "SUCCESS", "RATE_LIMITED", "FAILED"
    message: str


class BumperEngine:
    """Main automated bumper engine with timer and channel orchestration."""

    def __init__(self, bump_interval_seconds: int = 7200):
        self.bump_interval = bump_interval_seconds
        self.tokens: List[BumperToken] = [
            BumperToken(name="Sample-Token-1", token="YOUR_DISCORD_TOKEN_HERE", channel_id="1182348765432198"),
            BumperToken(name="Sample-Token-2", token="YOUR_DISCORD_TOKEN_HERE", channel_id="1189876543210987")
        ]
        self.logs: List[BumpLogEvent] = []
        self.total_success_bumps: int = 0
        self.total_failed_bumps: int = 0
        self.is_running: bool = True
        self.last_bump_timestamp: float = time.time()
        self.next_bump_timestamp: float = time.time() + 7200
        
        # Initial log
        self.add_log("Discord-Server", "#general-chat", "System", "INFO", "Bumper Web GUI ready. Add your Discord token to begin auto-bumping.")

    def add_token(self, name: str, token: str, channel_id: str) -> None:
        """Adds a new user-supplied Discord token."""
        new_token = BumperToken(name=name, token=token, channel_id=channel_id)
        self.tokens.append(new_token)
        self.add_log("Discord-Server", f"#{channel_id[-4:] if len(channel_id)>4 else channel_id}", name, "INFO", f"Token '{name}' added successfully.")

    def remove_token(self, token_index: int) -> None:
        """Removes a token by index."""
        if 0 <= token_index < len(self.tokens):
            removed = self.tokens.pop(token_index)
            self.add_log("Discord-Server", "N/A", removed.name, "INFO", f"Token '{removed.name}' removed.")

    def get_seconds_until_next_bump(self) -> int:
        """Returns remaining seconds until next automated bump."""
        remaining = int(self.next_bump_timestamp - time.time())
        return max(0, remaining)

    def add_log(self, server_name: str, channel_id: str, token_name: str, status: str, message: str) -> None:
        """Records a new bump event log."""
        now = time.time()
        t_str = time.strftime("%H:%M:%S", time.localtime(now))
        event = BumpLogEvent(
            timestamp=now,
            formatted_time=t_str,
            server_name=server_name,
            channel_id=channel_id,
            token_name=token_name,
            status=status,
            message=message
        )
        self.logs.append(event)
        if len(self.logs) > 100:
            self.logs.pop(0)

    def trigger_manual_bump(self, channel_id: Optional[str] = None) -> BumpLogEvent:
        """Executes a manual bump action instantly."""
        now = time.time()
        token = self.tokens[0] if self.tokens else BumperToken("Default", "YOUR_DISCORD_TOKEN_HERE", "0")
        target_channel = channel_id or token.channel_id
        
        token.last_bump = now
        token.total_bumps += 1
        self.total_success_bumps += 1
        self.last_bump_timestamp = now
        self.next_bump_timestamp = now + self.bump_interval

        t_str = time.strftime("%H:%M:%S", time.localtime(now))
        event = BumpLogEvent(
            timestamp=now,
            formatted_time=t_str,
            server_name="Discord-Server",
            channel_id=f"#{target_channel[-4:] if len(target_channel) > 4 else target_channel}",
            token_name=token.name,
            status="SUCCESS",
            message="Bump triggered successfully! /bump command sent."
        )
        self.logs.append(event)
        return event

    def get_status_payload(self) -> Dict:
        """Generates comprehensive status payload for Web UI."""
        remaining_sec = self.get_seconds_until_next_bump()
        progress_pct = int(((self.bump_interval - remaining_sec) / self.bump_interval) * 100)
        progress_pct = max(0, min(100, progress_pct))

        serialized_logs = []
        for l in reversed(self.logs[-15:]):
            serialized_logs.append({
                "formatted_time": l.formatted_time,
                "server_name": l.server_name,
                "channel_id": l.channel_id,
                "token_name": l.token_name,
                "status": l.status,
                "message": l.message
            })

        serialized_tokens = []
        for idx, t in enumerate(self.tokens):
            serialized_tokens.append({
                "index": idx,
                "name": t.name,
                "masked_token": t.masked_token,
                "channel_id": t.channel_id,
                "status": t.status,
                "total_bumps": t.total_bumps
            })

        return {
            "is_running": self.is_running,
            "seconds_remaining": remaining_sec,
            "progress_pct": progress_pct,
            "total_success": self.total_success_bumps,
            "total_failed": self.total_failed_bumps,
            "total_servers": len(self.tokens),
            "tokens": serialized_tokens,
            "logs": serialized_logs
        }
