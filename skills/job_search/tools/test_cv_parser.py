from skills.job_search.tools.cv_parser import parse_cv


file_path = "data/uploads/test_cv.pdf"


result = parse_cv(
    file_path
)

print(result)