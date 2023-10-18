def ResponseModel(data, message):
    return {
        "data": data,
        "message": message,
    }


def ErrorResponseModel(error, message):
    return {
        "error": error,
        "message": message,
    }


def ResponseHelper(snippet) -> dict:
    return {
        "id": str(snippet["_id"]),
        "title": snippet["title"],
        "code": snippet["code"],
        "language": snippet["language"],
        "tags": snippet["tags"],
        "favorite": snippet["favorite"],
        "createdAt": snippet["createdAt"],
        "updatedAt": snippet["updatedAt"],
    }
