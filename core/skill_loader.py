import os
import yaml


class SkillLoader:

    def __init__(self, skills_path="skills"):
        self.skills_path = skills_path
        self.skills = {}

    def load_skills(self):

        if not os.path.exists(self.skills_path):
            return {}

        for skill_name in os.listdir(self.skills_path):

            skill_dir = os.path.join(
                self.skills_path,
                skill_name
            )

            if not os.path.isdir(skill_dir):
                continue

            manifest_path = os.path.join(
                skill_dir,
                "skill.md"
            )

            if not os.path.exists(manifest_path):
                continue

            self.skills[skill_name] = self._parse_manifest(
                manifest_path
            )

        return self.skills


    def _parse_manifest(self, file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8-sig"
        ) as f:

            content = f.read()


        if content.startswith("---"):

            parts = content.split(
                "---",
                2
            )

            if len(parts) >= 3:

                yaml_content = parts[1]

                data = yaml.safe_load(
                    yaml_content
                )

                if data:
                    return data


        return {
            "name": os.path.basename(
                os.path.dirname(file_path)
            )
        }


skill_loader = SkillLoader()