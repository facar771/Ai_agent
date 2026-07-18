# core/budget_guard.py

import json
import os
from datetime import datetime

from core.config import settings


class BudgetGuard:
    def __init__(self):
        self.log_path = settings.SPEND_LOG
        self.max_budget = settings.MAX_BUDGET
        self.dry_run = settings.DRY_RUN

        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)

        if not os.path.exists(self.log_path):
            with open(self.log_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "total_spent": 0.0,
                        "calls": []
                    },
                    f,
                    indent=4
                )

    def _read_log(self) -> dict:
        with open(self.log_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write_log(self, data: dict) -> None:
        with open(self.log_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def is_dry_run(self) -> bool:
        return self.dry_run

    def can_call(self) -> bool:
        if self.dry_run:
            return True

        log = self._read_log()
        return log["total_spent"] < self.max_budget

    def log_usage(
        self,
        prompt_tokens: int,
        completion_tokens: int,
        total_tokens: int,
        cost: float
    ) -> None:

        if self.dry_run:
            return

        log = self._read_log()

        log["total_spent"] += cost

        log["calls"].append(
            {
                "timestamp": datetime.utcnow().isoformat(),
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens,
                "cost": round(cost, 6)
            }
        )

        self._write_log(log)

    def get_total_spent(self) -> float:
        log = self._read_log()
        return log["total_spent"]


budget_guard = BudgetGuard()