





var map = addtomap('map', true);
var map2 = addtomap('map2', false);


let initialbasemap = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map)
L.control.browserPrint({ title: 'MAP',position: 'topright' }).addTo(map)


// L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
//         attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
//     }).addTo(map2);


L.control.zoom({ position: 'topright' }).addTo(map);

map2.dragging.disable();
initComparisons();






function addtomap(mapdiv, zoomcontrol) {
   let mapcon =  L.map(mapdiv, {
        minZoom: 7,
        maxZoom: 20,
        zoomControl: false,
        //maxBounds: L.latLngBounds([8.1139, -1.2272], [9.1643, 1.0220]),
        measureControl: false,
    }).setView([8.799, -1], 8);
   return mapcon
}

function mapstate() {
   if (map) {
       map.invalidateSize();
   }
}

let compararray = []
function layerdefine(map, switchid, checkedid, rangerid, rangevalue, tilelayer, checkeddata) {
   $(rangerid).addClass('hidden');

   $('#'+switchid).on('change', function() {
     if (compararray.length  > 2){
      $(this).prop('checked', false);
     }
       checkedid = $(this).is(':checked');
       (tilelayer) ? layerTogglefunction(map, tilelayer, checkedid): layerTogglefunction(map, tilelayer, checkedid);
       if (checkedid) {
       
          $(rangerid).removeClass('hidden');
          selopt(switchid, checkedid);
          //compararray.push(switchid)
        // }else{

        // }
        
      } else { 
        $(rangerid).addClass('hidden');
        selopt(switchid, checkedid);
        //removearray(compararray, compararray)
      };

   });

   $(rangerid).on('change', function() {
       rangevalue = $(this).val();
       rangevalue == 0 ? tilelayer.setOpacity(0) : tilelayer.setOpacity(rangevalue / 10);
       tilelayer.setParams({}, false)
   });



   if (checkeddata) {
       tilelayer.addTo(map);
       $(rangerid).removeClass('hidden');
   };
}


function layerseldefine(mapm, layername, layername1) {
  if (layername1){
    mapm.removeLayer(layername1);
  }
   mapm.addLayer(layername);
   layername1 = layername
   return layername1
}



function selopt(switchid, status = false){
  $.get(`/apps/galamsey/changesel/?seloption=${switchid}&status=${status}`, function(data){$('#comparesel').html(data)});
}


function removearray(array, itemtoremove ){
  array.splice($.inArray(itemtoremove, array),1);
}
















function loadVectorlayerfunction(url, layername) {
   let loaddata;
   loaddata = L.tileLayer.wms(url, {
       layers: 'cite:' + layername,
       format: 'image/png',
       transparent: true,
   });
   return loaddata;

}




function layerTogglefunction(map, layername, visibility) {
   if (layername) {
       if (visibility == false) {
           map.removeLayer(layername);
       } else {
           map.addLayer(layername);

       }
   } else {
       alert('Layer is not defined');
   }
 }

