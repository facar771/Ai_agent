# skills/job_search/tools/job_matcher.py

from core.budget_guard import budget_guard


def run(
    cv_text: str,
    job_text: str,
    criteria: str
):

    prompt = f"""
CV:
{cv_text}

İş İlanı:
{job_text}

Kullanıcı Kriterleri:
{criteria}

Görev:
CV ile iş ilanını karşılaştır.
1-10 arasında uygunluk skoru ver.
Kısa gerekçe yaz.
"""

    response = budget_guard.call(
        prompt=prompt,
        max_output_tokens=300
    )

    return {
        "reply_text": response,
        "status": "ok"
    }