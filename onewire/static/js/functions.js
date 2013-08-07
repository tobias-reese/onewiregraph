function updateLastScan(container) {
    $.ajax("/api/last_scan").done(
        function (msg) {
            if (!msg) {
                container.text('Never');
            } else {
                container.text(msg);
            }
        }
    )
}

function scan(container) {
    $.ajax("/api/scan").done(
        function (data) {
            if (data) {
                container.empty();
                var content = "";
                $.each(data.states, function(i, value) {
                    content = content + "<h3>" + value[1] + "</h3>";
                    if (value[1] === 'unconfigured') {
                        content = content + "<div><table>";
                        for (var j=0;j<data[value[1]].length;j++) {
                            content = content + "<tr><td>" + data[value[1]][j] + '</td><td><button id="setup-' + data[value[1]][j] + '">Setup</button></td></tr>';
                        }
                        content = content + "</table></div>";
                    } else if (value[1] === 'configured') {
                        content = content + "<div><table>";
                        for (var j=0;j<data[value[1]].length;j++) {
                            content = content + "<tr><td>" + data[value[1]][j] + '</td></tr>';
                        }
                        content = content + "</table></div>";
                    } else {
                        content = content + "<div/>";
                    }
                });
                container.append(content);
                try {
                    container.accordion("option");
                    container.accordion("refresh");
                } catch  (e) {
                    container.accordion();
                } finally {
                    $('button[id^=setup-]').button();
                    $('button[id^=setup-]').click(setup);
                }
            }
        }
    )
}

function setup() {
    var id = this.id.replace("setup-", "");
    $.ajax("/sensor/add/"+id).done(
        function (msg) {
            if (msg) {
                $( "#settings_dialog" ).empty();
                $( "#settings_dialog" ).append(msg);
                //$( "#form_save").button();
                //$( "#form_save").click(setup_save);
                $( "#settings_dialog" ).dialog( "open" );
            }
        }
    )
    console.log(id);
}

function setup_save() {
    var data = $('form').serialize();
    $.ajax("/sensor/save", {
        type: "POST",
        data: data
    }).done()
    $( "#settings_dialog").dialog("close");
    scan($( "#sensor_settings" ));
    updateLastScan($( "#scan_label" ));
}