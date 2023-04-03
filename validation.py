def _validate_check_resume_request(request):
    data = request.json
    if not data.get("ext") or not data.get("fileUrl"):
        raise ValueError("fields ext and fileUrl is required")

    if data["ext"] not in ["pdf", "doc", "docx"]:
        raise ValueError(f"file type {data['ext']} not supported")

    return data["fileUrl"], data["ext"]
