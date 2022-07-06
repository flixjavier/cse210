from game.scripting.action import Action


class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        self._audio_service.load_sounds("C:/Users/felfl/Documents/cse210/cse210-projects/cse210/batter-incomplete/batter/assets/sounds")
        self._video_service.load_fonts("C:/Users/felfl/Documents/cse210/cse210-projects/cse210/batter-incomplete/batter/assets/fonts")
        self._video_service.load_images("C:/Users/felfl/Documents/cse210/cse210-projects/cse210/batter-incomplete/batter/assets/images")
        