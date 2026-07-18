# core/engine.py

from core.skill_loader import skill_loader
from core.router import router
from core.logger import logger

import importlib

from skills.job_search.tools.cv_parser import parse_cv


class AgentEngine:

    def __init__(self):
        self.skills = {}

    def initialize(self):

        self.skills = skill_loader.load_skills()

        router.update_skills(
            self.skills
        )

        logger.info(
            f"Loaded skills: {list(self.skills.keys())}"
        )

    def _execute_skill(
        self,
        skill_name: str,
        request: dict
    ):

        skill = self.skills.get(
            skill_name
        )

        if not skill:
            raise Exception(
                "Skill bulunamadı"
            )

        entry = skill.get(
            "entry"
        )

        if not entry:
            raise Exception(
                "Skill entry tanımlı değil"
            )

        module_name, function_name = entry.rsplit(
            ".",
            1
        )

        module = importlib.import_module(
            f"skills.{skill_name}.{module_name}"
        )

        function = getattr(
            module,
            function_name
        )

        cv_text = ""

        if request.get("file_path"):

            cv_text = parse_cv(
                request["file_path"]
            )

        return function(
            cv_text=cv_text,
            job_text=request.get(
                "text",
                ""
            ),
            criteria=request.get(
                "criteria",
                ""
            )
        )

    def run(
        self,
        request: dict
    ):

        text = request.get(
            "text",
            ""
        )

        skill_name = router.route(
            text
        )

        if not skill_name:
            return {
                "reply_text": "Uygun bir skill bulunamadı.",
                "status": "error"
            }

        try:

            return self._execute_skill(
                skill_name,
                request
            )

        except Exception as e:

            logger.error(
                str(e)
            )

            return {
                "reply_text": str(e),
                "status": "error"
            }


engine = AgentEngine()