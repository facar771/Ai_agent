# core/router.py

class SkillRouter:
    def __init__(self, skills=None):
        self.skills = skills or {}

    def update_skills(self, skills):
        self.skills = skills

    def route(self, text: str):

        print("GELEN TEXT:", text)
        print("SKILLS:", self.skills)

        if not text:
            return None

        text = text.lower()

        for skill_name, skill_data in self.skills.items():

            print("CONTROL SKILL:", skill_name)

            keywords = skill_data.get(
                "keywords",
                []
            )

            print("KEYWORDS:", keywords)

            for keyword in keywords:

                if keyword.lower() in text:
                    print("MATCH:", keyword)
                    return skill_name

        return None


router = SkillRouter()