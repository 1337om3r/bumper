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
    status: str = "Online"
    last_bump: Optional[float] = None
    total_bumps: int = 0

    @property
    def masked_token(self) -> str:
        """Returns masked token string for security."""
        if not self.token or self.token == "YOUR_DISCORD_TOKEN_HERE":
            return "discord.gg/A...YjK"
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
            BumperToken(name="Primary-Account", token="YOUR_DISCORD_TOKEN_HERE", channel_id="1182348765432198", total_bumps=142),
            BumperToken(name="Secondary-Alt", token="YOUR_DISCORD_TOKEN_HERE", channel_id="1189876543210987", total_bumps=88)
        ]
        now = time.time()
        self.logs: List[BumpLogEvent] = [
            BumpLogEvent(timestamp=now - 120, formatted_time="14:32:01", server_name="server-1", channel_id="#general-chat", token_name="discord.gg/A...YjK", status="SUCCESS", message="Bumped: server-1 #general (SUCCESS)"),
            BumpLogEvent(timestamp=now - 60, formatted_time="14:31:55", server_name="server-2", channel_id="#chat", token_name="discord.gg/T...5vR", status="SUCCESS", message="Bumped: server-2 #chat (SUCCESS)"),
            BumpLogEvent(timestamp=now - 30, formatted_time="14:29:48", server_name="server-3", channel_id="#main-chat", token_name="discord.gg/D...pP0", status="RATE_LIMITED", message="Error: Token failed (Rate Limited)")
        ]
        self.total_success_bumps: int = 142
        self.total_failed_bumps: int = 1
        self.is_running: bool = True
        self.last_bump_timestamp: float = time.time() - 3600
        self.next_bump_timestamp: float = time.time() + 86  # 1m 26s
        
    def add_token(self, name: str, token: str, channel_id: str) -> None:
        """Adds a new user-supplied Discord token."""
        new_token = BumperToken(name=name, token=token, channel_id=channel_id)
        self.tokens.append(new_token)
        self.add_log("Discord-Server", f"#{channel_id[-4:] if len(channel_id)>4 else channel_id}", name, "SUCCESS", f"Token '{name}' added and ready.")

    def remove_token(self, token_index: int) -> None:
        """Removes a token by index."""
        if 0 <= token_index < len(self.tokens):
            removed = self.tokens.pop(token_index)
            self.add_log("Discord-Server", "N/A", removed.name, "RATE_LIMITED", f"Token '{removed.name}' removed.")

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
        self.next_bump_timestamp = now + 7200

        t_str = time.strftime("%H:%M:%S", time.localtime(now))
        event = BumpLogEvent(
            timestamp=now,
            formatted_time=t_str,
            server_name="server-active",
            channel_id=f"#{target_channel[-4:] if len(target_channel) > 4 else target_channel}",
            token_name=token.name,
            status="SUCCESS",
            message="Manual bump triggered! /bump command dispatched."
        )
        self.logs.append(event)
        return event

    def get_status_payload(self) -> Dict:
        """Generates comprehensive status payload for Web UI."""
        remaining_sec = self.get_seconds_until_next_bump()
        progress_pct = int(((7200 - remaining_sec) / 7200) * 100)
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
            "total_servers": 12,
            "tokens": serialized_tokens,
            "logs": serialized_logs
        }
