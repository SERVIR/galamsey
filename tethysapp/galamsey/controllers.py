from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
import ee
from ee.ee_exception import EEException
from django.http import JsonResponse


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    # save_button = Button(
    #     display_text='',
    #     name='save-button',
    #     icon='glyphicon glyphicon-floppy-disk',
    #     style='success',
    #     attributes={
    #         'data-toggle':'tooltip',
    #         'data-placement':'top',
    #         'title':'Save'
    #     }
    # )

    # edit_button = Button(
    #     display_text='',
    #     name='edit-button',
    #     icon='glyphicon glyphicon-edit',
    #     style='warning',
    #     attributes={
    #         'data-toggle':'tooltip',
    #         'data-placement':'top',
    #         'title':'Edit'
    #     }
    # )

    # remove_button = Button(
    #     display_text='',
    #     name='remove-button',
    #     icon='glyphicon glyphicon-remove',
    #     style='danger',
    #     attributes={
    #         'data-toggle':'tooltip',
    #         'data-placement':'top',
    #         'title':'Remove'
    #     }
    # )

    # previous_button = Button(
    #     display_text='Previous',
    #     name='previous-button',
    #     attributes={
    #         'data-toggle':'tooltip',
    #         'data-placement':'top',
    #         'title':'Previous'
    #     }
    # )

    # next_button = Button(
    #     display_text='Next',
    #     name='next-button',
    #     attributes={
    #         'data-toggle':'tooltip',
    #         'data-placement':'top',
    #         'title':'Next'
    #     }
    # )

    # context = {
    #     'save_button': save_button,
    #     'edit_button': edit_button,
    #     'remove_button': remove_button,
    #     'previous_button': previous_button,
    #     'next_button': next_button
    # }






















    return render(request, 'galamsey/home.html')






def ajaxrequest(request):
    getyear = str(request.GET.get('selyear', 2015))
    toHTML = {}

    try:
        ee.Initialize()
    except Exception as e:
        # from oauth2client.service_account import ServiceAccountCredentials
        # credentials = ServiceAccountCredentials.from_p12_keyfile(
        # service_account_email='remote-sensing-211620@appspot.gserviceaccount.com',
        # filename='remote-sensing-211620-5889d1746dcb.p12',
        # private_key_password='notasecret',
        # scopes=ee.oauth.SCOPE + ' https://www.googleapis.com/auth/drive ')
        credentials = ee.ServiceAccountCredentials('remote-sensing-211620@appspot.gserviceaccount.com', 'remote-sensing-211620-c458b5b9ec13.json')
        ee.Initialize(credentials)


        #return HttpResponse('<b> Unable to find the server at accounts.google.com </b>')



    try:
        countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
        Ghana = countries.filter(ee.Filter.eq('Country', 'Ghana')).geometry()

        # Load a Landsat 8 collection for a single path-row.
        treecovermap = ee.Image('projects/servir-wa/services/charcoal_ghana/Savannah_TreeCoverIndex_' + getyear)#.filterDate(getyear+'-01-01', getyear+'-12-01')
        visParams = {'min':50, 'max':150, 'palette':'663300,EAEAAE,93DB70,2F4F2F'}
        idfeatures = treecovermap.getMapId(visParams)

        toHTML['mapid'] = idfeatures['mapid']
        toHTML['token'] = idfeatures['token']
    except Exception as e:
        #raise
        toHTML['mapid'] = 'error'
    
    
    return JsonResponse(toHTML, safe=False)




def changesel(request):
    toHTML = {}
    toHTML['seloption'] = str(request.GET.get('seloption'))
    toHTML['status'] = str(request.GET.get('status'))

    return render(request, 'galamsey/selbox.html', toHTML)
