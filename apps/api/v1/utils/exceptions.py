from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


# custom exception handler used by django rest framework.  Configured in settings.py
# this is used to handle all error message and add additional
# details if required.

def custom_exception_handler(exc):
    # calling default handler to extract data.
    response = exception_handler(exc)

    # dictionary to hold different kind of messages.
    message = dict()

    # this dictionary will hold api specific information.
    api = dict()

    api['version'] = 'v1'
    api['path'] = '/api/v1/'

    # Now add the HTTP status code to the response.
    if response is not None:

        if response.data['detail'] == "Invalid token":
            message['status_code'] = response.status_code

            message['result'] = 'error'

            message['info'] = 'Authorization token is invalid'

            response.data['detail'] = message

        response.data = {'response': response.data['detail'], 'api': api}

    return response


# exception for failed authentication.
class ExceptionAuthenticationFailed(APIException):
    # we can override response by adding a message dict and then assigning it to "default_details"
    # message = dict()
    #
    # message['status_code'] = status.HTTP_401_UNAUTHORIZED
    #
    # message['result'] = 'error'
    #
    # message['info'] = 'Invalid username or password.'

    # http status code we need to send.
    status_code = status.HTTP_401_UNAUTHORIZED

# default_detail = message


# exception if any field is missing.
class ExceptionDefault(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


# exception if any field is missing.
class ExceptionMissingFields(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


# exception if any field is missing.
class ExceptionUnknownError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


# exception if email entered is not valid.
class ExceptionEmailNotValid(APIException):
    status_code = status.HTTP_200_OK


# exception if username is already used by another user.
class ExceptionUsernameAlreadyExists(APIException):
    status_code = status.HTTP_409_CONFLICT


# exception if username does not exists.
class ExceptionUsernameDoesNotExists(APIException):
    status_code = status.HTTP_409_CONFLICT


# exception if username does not exists.
class ExceptionAccountNotActivated(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED


# exception if username does not exists.
class ExceptionPasswordNotMatch(APIException):
    status_code = status.HTTP_409_CONFLICT


# exception if username does not exists.
class ExceptionInvalidPasswordToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED


# exception if email is already used by another user.
class ExceptionEmailAlreadyExists(APIException):
    status_code = status.HTTP_409_CONFLICT


# exception for situation if we are not able to add new user for some reason.
class ExceptionUnableToAddUser(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


# exception when user account is not active
class ExceptionAccountNotActive(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED

