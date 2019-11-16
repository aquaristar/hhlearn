angular.module("course").service("courseServices", ['$http', '$sce','utilServices', function ($http, $sce, utilServices) {

    this.replaceMediaTags = function (raw_html, data, resource) {

        var courseData = data.courseData;
        var orgData = data.orgData;
        var utilData = data.utilData;
        var userData = data.userData;        
        var resourceData = resource;
        var mediaTags = [];

        var rxp = /{{([^}]+)}}/g;
        var html_to_process = raw_html;
        var curMatch;

        while (curMatch = rxp.exec(html_to_process)) {

            var tagToRepace = curMatch[0];
            var extractedTag = $.trim(curMatch[1]);
            var extractedTagInfo = extractedTag.split(":");
            var tagType = extractedTagInfo[0];
            var mediaID = parseInt(extractedTagInfo[1]);
            var dataType = extractedTagInfo[1];

            if (tagType == "COURSE_IMAGE") {
                var cdnURL = "/static/dashboard/courses/images/pages/";
                var imageToShow = _.findWhere(courseData.images, {id: mediaID});
                if (!_.isUndefined(imageToShow)) {
                    //var fullImageHTMLTag = '<img alt="' + imageToShow.alt + '" title="' + imageToShow.title + '" name="' + imageToShow.name + '" align="' + imageToShow.align + '" src="' + cdnURL + imageToShow.file_name + '"/>';
                    var fullImageHTMLTag = '<img alt="' + imageToShow.alt + '" title="' + imageToShow.title + '" name="' + imageToShow.name + '" align="' 
                    						+ imageToShow.align + '" src="' + cdnURL + imageToShow.file_name 
                    						+ '" style="border:solid '+ imageToShow.border + 'px;"/>';                    
                    var html_to_process = html_to_process.replace(tagToRepace, fullImageHTMLTag);
                }
                else {
                    var fullImageHTMLTag = '<div class="text-center"><span class="label label-danger">IMAGE NOT FOUND</span></div>';
                    var html_to_process = html_to_process.replace(tagToRepace, fullImageHTMLTag);
                }
                //console.log(cdnURL+imageToShow);
            }
            else if (tagType == "COURSE_BORDER_IMAGE") {
                var cdnURL = "/static/dashboard/courses/images/pages/";
                var imageToShow = _.findWhere(courseData.images, {id: mediaID});
                if (!_.isUndefined(imageToShow)) {
                    var fullImageHTMLTag = '<img alt="' + imageToShow.alt + '" title="' + imageToShow.title + '" name="' + imageToShow.name + '" align="' 
                    						+ imageToShow.align + '" src="' + cdnURL + imageToShow.file_name 
                    						+ '" style="border:solid '+ imageToShow.border + 'px;"/>';
                    var html_to_process = html_to_process.replace(tagToRepace, fullImageHTMLTag);
                }
                else {
                    var fullImageHTMLTag = '<div class="text-center"><span class="label label-danger">IMAGE NOT FOUND</span></div>';
                    var html_to_process = html_to_process.replace(tagToRepace, fullImageHTMLTag);
                }
                //console.log(cdnURL+imageToShow);
            }
            else if (tagType == "COURSE_VIDEO") {
                var cdnURL = "/static/dashboard/courses/videos/";
                var videoToShow = _.findWhere(courseData.videos, {id: mediaID});
                if (!_.isUndefined(videoToShow)) {
                    var fullVideoHTMLTag = '<video width="320" height="240" controls> <source src="' + cdnURL + videoToShow.name + '" type="video/mp4"><object data="movie.mp4" width="320" height="240"></object></video>';
                    var html_to_process = html_to_process.replace(tagToRepace, fullVideoHTMLTag);
                }
                else {
                    var fullVideoHTMLTag = '<div class="text-center"><span class="label label-danger">VIDEO NOT FOUND</span></div>';
                    var html_to_process = html_to_process.replace(tagToRepace, fullVideoHTMLTag);
                }
            }
            else if (tagType == "STATE_PHONE_LAWS") {
                var currentStateLaw = _.findWhere(utilData.state_cell_phone_laws, {state: userData.location.state.abbreviation});
                var additionalRows = '';                
                if (currentStateLaw == undefined) return;
                if (dataType == "ALL") {
                    var additionalRows = "";
                    _.each(utilData.state_cell_phone_laws, function (state_phone_law) {
                    	if (_.isNull(state_phone_law.footnote)) {
                            state_phone_law.footnote = "";
                        }
                        if (state_phone_law.state != currentStateLaw.state) {                            
                            additionalRows += "<tr>";
                            additionalRows += "<td class=\"col-lg-1\">" + state_phone_law.state + "<\/td>";
                            additionalRows += " <td class=\"col-lg-1\">" + state_phone_law.cell_handheld_ban + "<\/td>";
                            additionalRows += " <td class=\"col-lg-1\">" + state_phone_law.cell_bus_drivers + "<\/td>";
                            additionalRows += " <td class=\"col-lg-2\">" + state_phone_law.cell_novice_drivers + "<\/td>";
                            additionalRows += " <td class=\"col-lg-1\">" + state_phone_law.text_all_drivers + "<\/td>";
                            additionalRows += " <td class=\"col-lg-1\">" + state_phone_law.text_bus_drivers + "<\/td>";
                            additionalRows += " <td class=\"col-lg-2\">" + state_phone_law.text_novice_drivers + "<\/td>";
                            additionalRows += " <td class=\"col-lg-3\"> " + state_phone_law.footnote;
                            additionalRows += " <\/td>";
                            additionalRows += " <\/tr>";
                        }
                    });
                }

                var stateLawTable = "";
                stateLawTable += "<div class=\"row\">";
                stateLawTable += "		<div class=\"col-lg-12\">";
                stateLawTable += "			<div class=\"tabbable\">";
                stateLawTable += "				<ul class=\"nav nav-tabs nav-append-content\">";
                stateLawTable += "					<li role=\"presentation\" class=\"active\"><a href=\"#locationlaw\" aria-controls=\"locationlaw\" role=\"tab\" data-toggle=\"tab\"><i class=\"fa fa-phone-square\"><\/i>  " + userData.location.state.abbreviation + " Cell Phone Laws<\/a><\/li>";
                stateLawTable += "					<li role=\"presentation\"><a href=\"#statelaws\" aria-controls=\"statelaws\" role=\"tab\" data-toggle=\"tab\"><i class=\"fa fa-phone-square\"><\/i>&nbsp; All State Cell Phone Laws<\/a><\/li>";
                stateLawTable += "				<\/ul>";
                stateLawTable += "				<!-- \/tabs -->";
                stateLawTable += "				<div class=\"tab-content\">";
                stateLawTable += "					<div class=\"tab-pane active\" id=\"locationlaw\">";
                stateLawTable += "						<div class=\"table-responsive\">";
                stateLawTable += '						<table class="table table-bordered table-striped table-responsive table-condensed">';
                stateLawTable += "							<thead><tr>";
                stateLawTable += "									<th><div class=\"col-lg-1 text-center\">State<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-1\">Handheld Ban<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-1\">Bus Drivers<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-2\"> Novice Drivers<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-1\">All Drivers<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-1\"> Bus Drivers<\/div></th>";                
                stateLawTable += "									<th><div class=\"col-lg-2\"> Novice Drivers<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-3\">Footnote<\/div></th>";
                stateLawTable += "							</tr></thead>";
                stateLawTable += "							<tbody><tr>";
                stateLawTable += "										<td class=\"col-lg-1 text-center\">" + currentStateLaw.state + "<\/div>";
                stateLawTable += "										<td class=\"col-lg-1\">" + currentStateLaw.cell_handheld_ban + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-1\">" + currentStateLaw.cell_bus_drivers + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-2\">" + currentStateLaw.cell_novice_drivers + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-1\">" + currentStateLaw.text_all_drivers + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-1\">" + currentStateLaw.text_bus_drivers + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-2\">" + currentStateLaw.text_novice_drivers + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-3\"> " + currentStateLaw.footnote + "<\/td>";                
                stateLawTable += "									<\/tr>";                
                stateLawTable += "								<\/tbody>";                
                stateLawTable += "							<\/table>";
                stateLawTable += "						<\/div>";
                stateLawTable += "					</div>";
                stateLawTable += "					<div class=\"tab-pane\" id=\"statelaws\">";
                stateLawTable += "						<div class=\"table-responsive\">";
                stateLawTable += '						<table class="table table-bordered table-striped table-responsive table-condensed">';
                stateLawTable += "							<thead><tr>";
                stateLawTable += "									<th><div class=\"col-lg-1 text-center\">State<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-1\">Handheld Ban<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-1\">Bus Drivers<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-2\"> Novice Drivers<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-1\">All Drivers<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-1\"> Bus Drivers<\/div></th>";                
                stateLawTable += "									<th><div class=\"col-lg-2\"> Novice Drivers<\/div></th>";
                stateLawTable += "									<th><div class=\"col-lg-3\">Footnote<\/div></th>";
                stateLawTable += "							</tr></thead>";
                stateLawTable += "							<tbody><tr>";
                stateLawTable += "										<td class=\"col-lg-1 text-center\">" + currentStateLaw.state + "<\/div>";
                stateLawTable += "										<td class=\"col-lg-1\">" + currentStateLaw.cell_handheld_ban + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-1\">" + currentStateLaw.cell_bus_drivers + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-2\">" + currentStateLaw.cell_novice_drivers + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-1\">" + currentStateLaw.text_all_drivers + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-1\">" + currentStateLaw.text_bus_drivers + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-2\">" + currentStateLaw.text_novice_drivers + "<\/td>";
                stateLawTable += "										<td class=\"col-lg-3\"> " + currentStateLaw.footnote + "<\/td>";                
                stateLawTable += "									<\/tr>";
                stateLawTable += additionalRows;
                stateLawTable += "								<\/tbody>";
                stateLawTable += "";
                stateLawTable += "";
                stateLawTable += "							<\/table>";
                stateLawTable += "						<\/div>";
                stateLawTable += "					<\/div>";
                stateLawTable += "";
                stateLawTable += "				<\/div>";
                stateLawTable += "			<\/div>";
                stateLawTable += "";
                stateLawTable += "";
                stateLawTable += "		<\/div>";
                stateLawTable += "	<\/div>";
                var html_to_process = html_to_process.replace(tagToRepace, stateLawTable);

            } else if (tagType == "COURSE_RESOURCE_FORM") {    
            	resource = _.findWhere(resourceData, {id: parseInt(dataType)});            	
            	if (resource != undefined) {
            		var fullImageHTMLTag = "<a data-toggle='modal' style='color:#00ABDF' href='#resource_info_modal' ng-click='setCurrentResource(" + dataType + ")'>" +  resource.resource_name + "</a>";            		
            		var html_to_process = html_to_process.replace(tagToRepace, fullImageHTMLTag);
            	}            	
            } else if (tagType == "COURSE_RESOURCE_PUBLICATION") {   
            	resource = _.findWhere(resourceData, {id: parseInt(dataType)});  
            	if (resource != undefined) {
            		var fullImageHTMLTag = "<a data-toggle='modal' style='color:#E30613' href='#resource_info_modal' ng-click='setCurrentResource(" + dataType + ")'>" +  resource.resource_name + "</a>";            		         		
            		var html_to_process = html_to_process.replace(tagToRepace, fullImageHTMLTag);            		
            	}            
            } else if (tagType == "COURSE_RESOURCE_VIDEO") {        
            	resource = _.findWhere(resourceData, {id: parseInt(dataType)});
            	//ci_format = resource.video_cover_image.split(".")[1];            	
            	if (resource != undefined) {
	            	//var fullVideoHTMLTag = '<video width="320" height="240" controls poster="/static/resources/files/' + ci_format + '/' + resource.video_cover_image + '"><source src="' + "/static/resources/files/mp4/" + resource.id + '.mp4" type="video/mp4"><object data="movie.mp4" width="320" height="240"></object></video>';
	            	//var fullVideoHTMLTag = '<iframe src="//fast.wistia.net/embed/iframe/lkw79ur6hk" allowtransparency="true" frameborder="0" scrolling="no" class="wistia_embed" name="wistia_embed" allowfullscreen mozallowfullscreen webkitallowfullscreen oallowfullscreen msallowfullscreen width="320" height="180"></iframe><script src="//fast.wistia.net/assets/external/E-v1.js" async></script>';
	            	var fullVideoHTMLTag = resource.where_was_resource_obtained;
	            	var html_to_process = html_to_process.replace(tagToRepace, fullVideoHTMLTag);
	            }            	
            } else if (tagType == "COURSE_RESOURCE_LANG_PUBLICATION") {      
                resource = _.findWhere(resourceData, {id: parseInt(dataType)});
                if (resource != undefined) {
                    var fullImageHTMLTag = "<a data-toggle='modal' style='color:#E30613' href='#resource_info_modal' ng-click='setCurrentResource(" + dataType + ")'>" +  resource.resource_name_language + "</a>";                                  
                    var html_to_process = html_to_process.replace(tagToRepace, fullImageHTMLTag);                   
                }               
            } else if (tagType == "COURSE_RESOURCE_LANG_FORM") {    
                resource = _.findWhere(resourceData, {id: parseInt(dataType)});             
                if (resource != undefined) {
                    console.log(resource);
                    var fullImageHTMLTag = "<a data-toggle='modal' style='color:#00ABDF' href='#resource_info_modal' ng-click='setCurrentResource(" + dataType + ")'>" +  resource.resource_name_language + "</a>";                  
                    var html_to_process = html_to_process.replace(tagToRepace, fullImageHTMLTag);
                }               
            }
            
            // COURSE_VIDEOfound.push( curMatch[1] );
        }
        return html_to_process;
    };

    this.highlightGlossaryWords = function (raw_html, data) {
        var raw_html = raw_html;
        //var paragraphs = $(raw_html).getElementsByTagName("p");
      /*  for(var i = 0; i < paragraphs.length; i++)
        {
            alert(paragraphs[i].innerHTML);
        }
       */
      //  _.each(data.courseData.glossary_words, function (glossary_word) {
           //var rxp = new RegExp("\b"+glossary_word.word+"\b", "gi");
            //var rxp = new RegExp("\\b"+glossary_word.word+"\\b","ig");
           // raw_html = raw_html.replace(rxp, "<span popover-trigger=\"mouseenter\"  popover-placement=\"top\" popover-title=\""+glossary_word.syllable+"\"  popover=\""+glossary_word.definition+"\" class=\"highlight_glossary_word\">$&</span>");


     //   });
        return raw_html;
    };

}]);