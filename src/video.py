from src.channel import Channel


class Video(Channel):

    def __init__(self, video_id: str):

        #super().__init__(channel_id)
        self.youtube = Channel.get_service()

        self.video = self.youtube.videos().list(part='snippet, statistics, contentDetails, topicDetails',
                                                id=video_id
                                                ).execute()

        self.video_id = video_id
        self.video_title: str = self.video["items"][0]["snippet"]["title"]
        self.video_url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.view_count: int = self.video["items"][0]["statistics"]["viewCount"]
        self.like_count: int = self.video["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Channel):
    def __init__(self, video_id: str, playlist_id: str):
        # super().__init__(channel_id)
        self.youtube = Channel.get_service()

        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                                 part='contentDetails, snippet',
                                                                 maxResults=50,
                                                                 ).execute()

        for video in self.playlist_videos["items"]:
            if video['contentDetails']['videoId'] == video_id:
                self.video_id = video_id
                self.playlist_id = playlist_id
                self.video_url = f"https://www.youtube.com/watch?v={self.video_id}"
                self.video_title: str = video["snippet"]["title"]

    def __str__(self):
        return f"{self.video_title}"
