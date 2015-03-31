$(document).ready(function() {
    var page_path = document.location.hash.replace(/^#/, '')
    updateBreadCrumbs(page_path)

    table = $(filechooser_id).dataTable( {
        "sorting": [],
        "language": {
          "emptyTable":     "empty directory"
        },
        "ajax":       baseurl + page_path,
        "columns": [
            { "render": function ( value, type, data, meta ) {
                file = data['filename']
                if (type == 'display'){
                  url = (file['type'] == 'folder')  ? '#'+file['value'] : nexturl + encodeURI(file['value']);

                  content = "<span class=\"glyphicon glyphicon-"+file['icon']+"\" aria-hidden=\"true\"></span> &nbsp;";
                  return content + ' <a href="'+url+'" data-file-name="'+file['value']+'" class="file-type-'+file['type']+'">' + file['display'] + '</a>';
                }
                else
                  return data['filename']['value'];
            }, },
            { "render": function ( value, type, data, meta ) {
                  if (type == 'display'){
                    return '<span title="'+data['size']['value']+' bytes">' + data['size']['display'] + '</span>';
                  }
                  else return data['size']['value'];
            }, },
            { "render": function ( value, type, data, meta ) {
                  if (type == 'display'){
                    return '<span title="'+data['mtime']['title']+'">' + data['mtime']['display'] + '</span>';
                  }
                  else return data['mtime']['value'];
              },
            }
        ]
    } );

    // Add event for clicking on folders
    $(filechooser_id + ' tbody').on('click', 'a.file-type-folder', function () {
        changeDirectory($(this).data('file-name'))
    });

    // Add event for clicking on breadcrumbs
    $('#folder-breadcrumbs').on('click', 'a', function () {
        changeDirectory($(this).data('full-path'))
    });

    $(window).on('hashchange', function(){
          var page_path = document.location.hash.replace(/^#/, '')
          changeDirectory(page_path)
    });

    function changeDirectory(new_path){
      updateBreadCrumbs(new_path)
      table.api().ajax.url(baseurl + encodeURI(new_path)).load();
    }

    function updateBreadCrumbs(local_path){
      breadcrumbs = $('#folder-breadcrumbs')
      breadcrumbs.empty()

      // add first '/'
      if (local_path[0] != '/')
        local_path = '/' + local_path

      // remove trailing '/'
      if (local_path[local_path.length-1] == '/')
        local_path = local_path.substring(0, local_path.length-1)

      paths = local_path.split("/");
      full_path = ''
      for (i = 0; i < paths.length - 1; i++)
      {
        folder = paths[i]
        breadcrumbs.append( '<li><a href="#'+full_path+folder+'" data-full-path="'+full_path+folder+'">'+print_dir_name(folder)+'</a></li>' );
        if (folder) full_path += folder + '/'
      }

      // add active node
      breadcrumbs.append( '<li class="active">'+print_dir_name(paths[paths.length-1])+'</li>' );
    }

    function print_dir_name(name){
      if (name == "") return '<span class="glyphicon glyphicon-home" aria-hidden="true"></span>';
      else return name;
    }
} );
