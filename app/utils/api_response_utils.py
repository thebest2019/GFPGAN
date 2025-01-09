def create_api_response(client_id, is_success=True, message="", payload=None):
    """
    Creates a response dictionary similar to the C# ApiResponse<T> class.
    """
    return {
        "ClientId": client_id,
        "IsSuccess": is_success,
        "Message": message,
        "Payload": payload
    }