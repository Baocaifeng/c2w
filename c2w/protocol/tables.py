type_code = {
        "loginRequest": 0,
        "movieList": 3,
        "userList": 5,
        "disconnectRequest": 15,
        "message": 1,
        "messageForward": 12,
        "roomRequest": 8,
        "privateChateRequest": 10,
        "leavePrivateChatRequest": 7,
        "leavePrivateChatRequestForward": 9,
        "AYT": 6,
        "errorMessage": 14
        }

room_type = {
        "mainRoom": 0,
        "movieRoom": 1,
        "privateChat": 2,
        "notApplicable": 3
        }

error_code = {
        "userNotAvailable": 1,
        "idNotExist": 2,
        "serverFilled": 3,
        "messageTooLong": 4,
        "privateChatRequestRejected": 5,
        "invalidMessage": 6
        }

# state of a client
state_code = {
        "disconnected": 0,
        "loginWaitForMovieList": 1,
        "loginWaitForUserList": 2,
        "loginWaitForAck": 4,
        "inMainRoom": 3
        }

type_decode = {
        0: "loginRequest",
        3: "movieList",
        5: "userList",
        15: "disconnectRequest",
        1: "message",
        12: "messageForward",
        8: "roomRequest",
        10: "privateChateRequest",
        7: "leavePrivateChatRequest",
        9: "leavePrivateChatRequestForward",
        6: "AYT",
        14: "errorMessage"
        }


err_decode = {
        1: "usernameNotAvailable",
        2: "idNotExist",
        3: "serverFilled",
        4: "messageTooLong",
        5: "privateChatRequestRejected",
        6: "invalidMessage"
        }

room_type_decode = {
        0: "mainRoom",
        1: "movieRoom",
        2: "privateChat",
        3: "notApplicable"
        }
