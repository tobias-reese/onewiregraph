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

function update_data(container) {
    container.empty()
    $.ajax("/api/sensors").done(
        function (msg) {
            var data_content = ''
            $.each(msg.configured, function(i, value) {
                data_content = data_content + "<h3>" + value + "</h3>"
                data_content = data_content + "<h4>Last 2 Hours</h4>"
                data_content = data_content + "<img src=\"/static/" + value + "/hour.png\"/>"
                data_content = data_content + "<h4>Last day</h4>"
                data_content = data_content + "<img src=\"/static/" + value + "/day.png\"/>"
                data_content = data_content + "<h4>Last week</h4>"
                data_content = data_content + "<img src=\"/static/" + value + "/week.png\"/>"
                data_content = data_content + "<h4>Last month</h4>"
                data_content = data_content + "<img src=\"/static/" + value + "/month.png\"/>"
                data_content = data_content + "<h4>Last year</h4>"
                data_content = data_content + "<img src=\"/static/" + value + "/year.png\"/>"
            })
            container.append(data_content)
        }
    )
    // http://172.30.10.243:8000/static/10-000802909647/hour.png
}