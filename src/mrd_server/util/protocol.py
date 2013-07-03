# -*- coding: utf-8 -*-

class ResultCodes(object):
    """docstring for ResultCodes"""
    (
        Success,
        NicknameExist,
        NicknameNonExist,
        UserPasswordWrong,
        InputParamError,
        SessionIdNonExist,
        SessionIdExpired,
        NoData,
        GameVersionError,
        DBInputError,
        DataExist,
        ShortNickname,
        ShortPassword
    ) = range(100, 113)

    AccessError = 200


class ProtocolTypes(object):
    """docstring for ProtocolTypes"""
    (
        RegisterUser, LoginUser, CreateCharacter, GetNotice,
        GetCharacter, CheckGameVersion, AddFriend, GetFriendsList,
        FindFriendByName, GetInventories, SetInventories,
        GetSlots, SetSlots, GetStats, SetStats, WriteMail, ReadMail,
        GetGiftMail, GetMailList, DeleteMails, SetOwnCostumes, GetOwnCostumes,
        GetOwnCostumeBases, SetOwnCostumeBases, RequestFriend,
        GetWaitingFriends, AcceptFriend, GetFriendCharacterInfo,
        AddCompletedEvent, GetFishing, AddOwnCostume, AddOwnCostumeBase,
        SendFriendShipPoint, ReceiveFriendShipPoint,
        SetButtonState, GetButtonState, SetSavedStory, GetSavedStory,
        SetSavedCurrentZone, GetSavedCurrentZone,
        AddPuzzlePiece, GetPuzzlePieces, AddPuzzle, GetPuzzles,
        AddDiary, GetDiaries, SetWornCostume, GetWornCostume,
        SetCash, GetCash,
    ) = range(100, 150)