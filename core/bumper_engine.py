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
            BumperToken(name="Primary-Account", token="MTI0OTg3MjM0OTg3MjM0.G9x0.DemoTokenKeyAlpha", channel_id="1182348765432198"),
            BumperToken(name="Secondary-Alt", token="OTg3NjU0MzIxMDk4NzY1.H1y2.DemoTokenKeyBeta", channel_id="1189876543210987")
        ]
        self.logs: List[BumpLogEvent] = []
        self.total_success_bumps: int = 142
        self.total_failed_bumps: int = 1
        self.is_running: bool = True
        self.last_bump_timestamp: float = time.time() - 3600
        self.next_bump_timestamp: float = time.time() + 3600
        
        # Initial seed log
        self.add_log("Discord-Server-1", "#general-chat", "Primary-Account", "SUCCESS", "Autobump triggered successfully via /bump")

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
        token = self.tokens[0] if self.tokens else BumperToken("Default", "token", "0")
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
            server_name="Discord-Server-Active",
            channel_id=f"#{target_channel[-4:] if len(target_channel) > 4 else target_channel}",
            token_name=token.name,
            status="SUCCESS",
            message="Manual bump triggered! /bump command dispatched successfully."
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
        for t in self.tokens:
            serialized_tokens.append({
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
