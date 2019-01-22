from tethys_sdk.base import TethysAppBase, url_map_maker


class Galamsey(TethysAppBase):
    """
    Tethys app class for galamsey.
    """

    name = 'galamsey'
    index = 'galamsey:home'
    icon = 'galamsey/images/icon.gif'
    package = 'galamsey'
    root_url = 'galamsey'
    color = '#2980b9'
    description = 'galamsey app'
    tags = '&quot;Hydrology&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='galamsey',
                controller='galamsey.controllers.home'
            ),

            UrlMap(
                name='ajaxrequest',
                url='ajaxrequest',
                controller='galamsey.controllers.ajaxrequest'
            ),

                UrlMap(
                name='changesel',
                url='changesel',
                controller='galamsey.controllers.changesel'
            ),
        )

        return url_maps
