from .configs import *
import requests
import json


class Telegram:
    def bot(self, telegram_method, data, method='GET', file=None):
        if PROXY_HTTP:
            proxy_s = {
                "https": PROXY_HTTP,
                "http": PROXY_HTTP
            }
        if PROXY_SOCKS:
            proxy_s = {
                "http": f'socks5h://{PROXY_SOCKS}',
                "https": f'socks5h://{PROXY_SOCKS}'
            }
        try:
            url = f'https://api.telegram.org/bot{TOKEN}/{telegram_method}'
            if method == 'GET':
                request = requests.get(url, params=data, proxies=proxy_s)
                return json.loads(request.text)
            else:
                params = {"caption": data.pop("caption")}
                request = requests.post(
                    url, data=data, params=params, files=file, timeout=100)
                return json.loads(request.text)
        except Exception as error:
            print("Error in Telegram Class: ", error)

    def send_Message(self, chat_id, text, **kwargs):
        """
            This Method for sending message in telegram.
            **kwargs : 
                parse_mode-> Str , 
                entities-> List , 
                disable_web_page_preview -> Bool , 
                disable_notification = > Bool , 
                protect_content -> Bool , 
                reply_to_message_id - > Int , 
                allow_sending_without_reply -> Bool , 
                reply_markup - > List , 
        """
        params = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "html",
            "disable_web_page_preview": "true"
        }
        params.update(**kwargs)
        result = self.bot("sendMessage", params)
        return result

    def editMessageText(self, chat_id, message_id, text, **kwargs):
        """
            This Method for sending message in telegram.
            **kwargs : 
                parse_mode-> Str , 
                entities-> List , 
                disable_web_page_preview -> Bool , 
                disable_notification = > Bool , 
                protect_content -> Bool , 
                reply_to_message_id - > Int , 
                allow_sending_without_reply -> Bool , 
                reply_markup - > List , 
        """
        params = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text,
            "parse_mode": "html",
            "disable_web_page_preview": "true"
        }

        params.update(**kwargs)
        result = self.bot("editMessageText", params)
        return result

    def forward_Message(self, chat_id, from_chat_id, message_id: int, **kwargs):
        """
        This Method for forward message in telegram.
            **kwargs : 
                disable_notification - > Bool , 
                protect_content - > Bool
        """
        params = {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id
        }
        params.update(**kwargs)
        result = self.bot("forwardMessage", params)
        return result

    def copy_Message(self, chat_id, from_chat_id, message_id: int, **kwargs):
        """
        This Method for Copy message in telegram.
            **kwargs : 
                caption -> Str , 
                parse_mode -> Str , 
                caption_entities -> List , 
                disable_notification -> Bool , 
                protect_content -> Bool , 
                reply_to_message_id -> Int , 
                allow_sending_without_reply -> Bool , 
                reply_markup -> List , 
        """
        params = {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id
        }
        params.update(**kwargs)
        result = self.bot("copyMessage", params)
        return result

    def send_Photo(self, chat_id, photo, **kwargs):
        """
        This Method for send_Photo in telegram.
            **kwargs : 
                caption -> Str , 
                parse_mode -> Str , 
                caption_entities -> List , 
                disable_notification -> Bool , 
                protect_content -> Bool , 
                reply_to_message_id -> Int , 
                allow_sending_without_reply -> Bool , 
                reply_markup -> List , 
        """
        # print(type(photo))
        method = 'GET'
        if isinstance(photo, bytes):
            method = 'POST'

        params = {
            "chat_id": str(chat_id),
            "photo": photo
        }
        # print(method)
        params.update(**kwargs)
        result = self.bot("sendPhoto", params, method)
        return result

    def send_Audio(self, chat_id, audio, **kwargs):
        """
        This Method for send_Audio in telegram.
            **kwargs : 
                caption -> Str , 
                parse_mode -> Str , 
                caption_entities -> List , 
                disable_notification -> Bool , 
                protect_content -> Bool , 
                reply_to_message_id -> Int , 
                allow_sending_without_reply -> Bool , 
                reply_markup -> List , 
                duration -> Int ,
                performer -> Str ,
                title  -> Str ,
                thumb  -> Str & File ,
        """
        method = 'GET'
        if isinstance(audio, bytes):
            method = 'POST'

        params = {
            "chat_id": str(chat_id),
            "audio": audio
        }
        # print(method)
        params.update(**kwargs)
        result = self.bot("sendAudio", params, method)
        return result

    def send_Document(self, chat_id, document, **kwargs):
        """
        This Method for send_Document in telegram.
            **kwargs : 
                caption -> Str , 
                parse_mode -> Str , 
                caption_entities -> List , 
                disable_content_type_detection -> Bool ,
                disable_notification -> Bool , 
                protect_content -> Bool , 
                reply_to_message_id -> Int , 
                allow_sending_without_reply -> Bool , 
                reply_markup -> List , 
        """
        method = 'POST'
        params = {
            "chat_id": str(chat_id)
        }
        file = {
            "document": document
        }
        params.update(**kwargs)
        result = self.bot("sendDocument", params, method, file)
        return result

    def send_Video(self, chat_id, video, **kwargs):
        """
        This Method for send_Video in telegram.
            **kwargs : 
                caption -> Str , 
                parse_mode -> Str , 
                caption_entities -> List , 
                disable_content_type_detection -> Bool ,
                disable_notification -> Bool , 
                protect_content -> Bool , 
                reply_to_message_id -> Int , 
                allow_sending_without_reply -> Bool , 
                reply_markup -> List , 
                duration -> Int ,
                width -> Int ,
                height -> Int ,
                thumb  -> Str & File ,
                supports_streaming  -> Bool ,

        """
        method = 'GET'
        if isinstance(video, bytes):
            method = 'POST'

        params = {
            "chat_id": str(chat_id),
            "video": video
        }
        params.update(**kwargs)
        result = self.bot("sendVideo", params, method)
        return result

    def send_Animation(self, chat_id, animation, **kwargs):
        """
        This Method for send_Animation in telegram.
            **kwargs : 
                caption -> Str , 
                parse_mode -> Str , 
                caption_entities -> List , 
                disable_content_type_detection -> Bool ,
                disable_notification -> Bool , 
                protect_content -> Bool , 
                reply_to_message_id -> Int , 
                allow_sending_without_reply -> Bool , 
                reply_markup -> List , 
                duration -> Int ,
                width -> Int ,
                height -> Int ,
                thumb  -> Str & File ,
        """
        method = 'GET'
        if isinstance(animation, bytes):
            method = 'POST'

        params = {
            "chat_id": str(chat_id),
            "animation": animation
        }
        params.update(**kwargs)
        result = self.bot("sendAnimation", params, method)
        return result

    def send_Voice(self, chat_id, voice, **kwargs):
        """
        This Method for send_Voice in telegram.
            **kwargs : 
                caption -> Str , 
                parse_mode -> Str , 
                caption_entities -> List , 
                disable_content_type_detection -> Bool ,
                disable_notification -> Bool , 
                protect_content -> Bool , 
                reply_to_message_id -> Int , 
                allow_sending_without_reply -> Bool , 
                reply_markup -> List , 
                duration -> Int ,
                thumb  -> Str & File ,

        """
        method = 'GET'
        if isinstance(voice, bytes):
            method = 'POST'

        params = {
            "chat_id": str(chat_id),
            "voice": voice
        }

        params.update(**kwargs)
        result = self.bot("sendVoice", params, method)
        return result

    def send_VideoNote(self, chat_id, video_note, **kwargs):
        """
        This Method for send_VideoNote in telegram.
            **kwargs : 
                disable_notification -> Bool , 
                protect_content -> Bool , 
                reply_to_message_id -> Int , 
                allow_sending_without_reply -> Bool , 
                reply_markup -> List , 
                duration -> Int ,
                thumb  -> Str & File ,
                length -> Int
        """
        method = 'GET'
        if isinstance(video_note, bytes):
            method = 'POST'

        params = {
            "chat_id": str(chat_id),
            "video_note": video_note
        }

        params.update(**kwargs)
        result = self.bot("sendVideoNote", params, method)
        return result

    def send_MediaGroup(self, chat_id, media: list, **kwargs):
        """
        This Method for send_MediaGroup in telegram.
            **kwargs : 
                disable_notification -> Bool , 
                protect_content -> Bool , 
                reply_to_message_id -> Int , 
                allow_sending_without_reply -> Bool , 
        """
        method = 'GET'
        if isinstance(media[0], bytes):
            method = 'POST'

        params = {
            "chat_id": str(chat_id),
            "media": media
        }

        params.update(**kwargs)
        result = self.bot("sendMediaGroup", params, method)
        return result

    def send_AnswerCallbackQuery(self, callback_query_id, text: str, **kwargs):
        """
        This Method for send_AnswerCallbackQuery in telegram.
            **kwargs : 
                show_alert -> Bool , 
                url -> text , 
                cache_time -> Int , 
        """
        method = 'GET'

        params = {
            "callback_query_id": str(callback_query_id),
            "text": text
        }

        params.update(**kwargs)
        result = self.bot("answerCallbackQuery", params, method)
        return result

    def delete_Message(self, chat_id, message_id: int):
        """
        This Method for delete_Message in telegram.

        """
        method = 'GET'
        params = {
            "chat_id": str(chat_id),
            "message_id": message_id
        }

        result = self.bot("deleteMessage", params, method)
        return result

    def user_Joined(self, chat_id, user_id):
        """
            Use this method to get information about a member of a chat.
            Returns a ChatMember object on success.
        """
        method = 'GET'
        params = {
            "chat_id": str(chat_id),
            "user_id": str(user_id)
        }

        result = self.bot("getChatMember", params, method)
        # print(result)
        return result
