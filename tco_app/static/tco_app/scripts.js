document.addEventListener('DOMContentLoaded', () => {
    (function() {
        'use strict';
        window.addEventListener('load', function() {
            // Fetch all the forms we want to apply custom Bootstrap validation styles to
            var forms = document.getElementsByClassName('needs-validation');
            // Loop over them and prevent submission
            var validation = Array.prototype.filter.call(forms, function(form) {
                form.addEventListener('submit', function(event) {
                    if (form.checkValidity() === false) {
                        event.preventDefault();
                        event.stopPropagation();
                    }
                    form.classList.add('was-validated');
                }, false);
            });
        }, false);
    })();
    
    $("select#allsystems").on('change', function() {
        if ($(this).val() == 0) {
            $("#divModels").css('display', 'none');
            $("#divCpus").css('display', 'none');
            $("#lblCpu").css('display', 'none');
            $("#divPay").css('display', 'none');
            $("#btnSim").css('display', 'none');
            $("#divCurrency").css('display', 'none');
            $("#divMemory").css('display', 'none');
		}
        else {
            var url = "/simulation_page/" + $(this).val() + "/all_json_models/";
            $.getJSON(url, function(models) {
                // console.log(JSON.stringify(models));
                var options = '<option selected value="0">Select Model</option>';
                for (var i = 0; i < models.length; i++) {
                    options += '<option value="' + models[i].pk + '">' + models[i].fields["model_name"] + '</option>';
				}
                $("#divModels").css('display', 'block');
                $("select#allmodels").html(options);
                $("select#allmodels option:first").attr('selected', 'selected');
            });
            $("#divCpus").css('display', 'none');
            $("#lblCpu").css('display', 'none');
            $("#divPay").css('display', 'none');
            $("#btnSim").css('display', 'none');
            $("#divCurrency").css('display', 'none');
            $("#divMemory").css('display', 'none');
		}
    });
    
    $("select#allmodels").on('change', function() {
        if ($(this).val() == 0) {
            $("#divCpus").css('display', 'none');
            $("#lblCpu").css('display', 'none');
            $("#divPay").css('display', 'none');
            $("#btnSim").css('display', 'none');
            $("#divCurrency").css('display', 'none');
            $("#divMemory").css('display', 'none');
		}
        else {
            $("#divMemory").css('display', 'none');
            var url = "/simulation_page/" + $(this).val() + "/all_json_cpus/";
            $.getJSON(url, function(cpus) {
                var options = '<option selected value="">Select CPU</option>';
                var optionsmem = '<option selected value="">Select Memory</option>';
                // console.log(JSON.stringify(cpus));
                // console.log(cpus[0])
                if (cpus.length == 1)
                {
                    $("#cpulabel").val(cpus[0].id_cpu_value);
                    $("#cpulabel").attr('cpuid', cpus[0].pk);
                    $("#lblCpu").css('display', 'block');
                    $("#divCpus").css('display', 'none');
                    $("#divMemory").css('display', 'none');
				}
                else {
                    let previouslabel = '';

					for (var i = 0; i < cpus.length; i++) {
                        let labelcpu = cpus[i].id_cpu_value;
                        
                        if (previouslabel != labelcpu)
                        {
                            options += '<option value="' + cpus[i].pk + '">' + labelcpu + '</option>';
                            previouslabel = labelcpu;
                        }

                        $("select#allcpus").html(options);
                        $("select#allcpus option:first").attr('selected', 'selected');
                        $("#lblCpu").css('display', 'none');
                        $("#divCpus").css('display', 'block');
                        // $("#divMemory").css('display', 'none');

                        if (cpus[i].id_memory_value > 0)
                        {
                            let labelmem = cpus[i].id_memory_value;
						
                            optionsmem += '<option value="' + cpus[i].pk + '">' + labelmem + '</option>';
                            $("select#allMemory").html(optionsmem);
                            $("select#allMemory option:first").attr('selected', 'selected');
                            $("#divMemory").attr('hasmem', '1');
                        }
                        else
                        {
                            $("#divMemory").attr('hasmem', '0');
                            $("select#allMemory").html(optionsmem);
                        }
					}        
				}
                $("#divPay").css('display', 'block');
                $("#btnSim").css('display', 'block');
                $("#divCurrency").css('display', 'block');
            });
		}
    });	
    
    $("select#allcpus").on('change',  function() {
        if ($("#divMemory").attr('hasmem') == '1')
            $("#divMemory").css('display', 'block');
        else
        $("#divMemory").css('display', 'none');

    });
	
    $("#frmSim").on('submit',  function(event) {
        event.preventDefault();
        pay = $('#txtPay').val();
        coin = $("select#allcurrency option:selected").val();
        var idcpu;
        if ($('#lblCpu').css('display') == 'block')
                idcpu = $('#cpulabel').attr('cpuid');
        else
            idcpu = $("#allcpus option:selected" ).val();

        if (pay != "" && coin != "" && idcpu != "") {      
            payperyear = $('#txtPay').val();
            currency = $( "#allcurrency option:selected" ).val();
            var url = "/simulation_page/" + idcpu + "/" + payperyear + "/" + currency + "/json_simulation/";
            $.getJSON(url, function(savings) {
                console.log(JSON.stringify(savings));
                $("#divSearch").css('display', 'none');
                $("#divResults").css('display', 'block');
                $("#lblf_total_savings_currency").html(savings.f_total_savings_currency);
                $("#lblreduction_of").html(savings.reduction_of);
                $("#lbli_power_savings").html(savings.i_power_savings);
                $("#lbli_carbon_footprint_legacy").html(savings.i_carbon_footprint_legacy);
                $("#lbli_carbon_footprint_savings").html(savings.i_carbon_footprint_savings);
            })
            // **************************************
            // error handling
            // .done(function() { alert('getJSON request succeeded!'); })
            // .fail(function(jqXHR, textStatus, errorThrown) { alert('getJSON request failed! ' + textStatus); })
            // .always(function() { alert('getJSON request ended!'); });
        }
	});
});