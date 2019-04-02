document.addEventListener('DOMContentLoaded', () => {
    (function() {
        'use strict';
        window.addEventListener('load', function() {
            // Fetch all the forms we want to apply custom Bootstrap validation styles to
            let forms = document.getElementsByClassName('needs-validation');
            // Loop over them and prevent submission
            let validation = Array.prototype.filter.call(forms, function(form) {
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
		}
        else {
            let url = "/simulation_page/" + $(this).val() + "/all_json_models/";
            $.getJSON(url, function(models) {
                // console.log(JSON.stringify(models));
                let options = '<option selected value="0">Select Model</option>';
                for (let i = 0; i < models.length; i++) {
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
            let url = "/simulation_page/" + $(this).val() + "/all_json_cpus/";
            $.getJSON(url, function(cpus) {
                let options = '<option selected value="">Select CPU</option>';
                if (cpus.length == 1)
                {
                    $("#cpulabel").val(cpus[0].id_cpu_value);
                    $("#cpulabel").attr('cpuid', cpus[0].pk);
                    $("#lblCpu").css('display', 'block');
                    $("#divCpus").css('display', 'none');
                    $("#divMemory").css('display', 'none');
				}
                else {
					for (let i = 0; i < cpus.length; i++) {
                        let labelcpu = cpus[i].id_cpu_value;
                        // console.log(cpus[i])

                        if (cpus[i].id_memory_value != '0')
                            labelcpu = labelcpu + ' (' + cpus[i].id_memory_value + ')';

                        options += '<option value="' + cpus[i].pk + '">' + labelcpu + '</option>';

                        $("select#allcpus").html(options);
                        $("select#allcpus option:first").attr('selected', 'selected');
                        $("#lblCpu").css('display', 'none');
                        $("#divCpus").css('display', 'block');
					}        
				}
                $("#divPay").css('display', 'block');
                $("#btnSim").css('display', 'block');
                $("#divCurrency").css('display', 'block');
            });
		}
    });	
	
    $("#frmSim").on('submit',  function(event) {
        event.preventDefault();
        pay = $('#txtPay').val();
        coin = $("select#allcurrency option:selected").val();
        let idcpu;
        if ($('#lblCpu').css('display') == 'block')
                idcpu = $('#cpulabel').attr('cpuid');
        else
            idcpu = $("#allcpus option:selected" ).val();

        if (pay != "" && coin != "" && idcpu != "") {      
            payperyear = $('#txtPay').val();
            currency = $( "#allcurrency option:selected" ).val();
            let url = "/simulation_page/" + idcpu + "/" + payperyear + "/" + currency + "/json_simulation/";
            $.getJSON(url, function(savings) {
                // console.log(JSON.stringify(savings));
                $("#divSearch").css('display', 'none');
                $("#divResults").css('display', 'block');
                $("#lblf_total_savings_currency").html(savings.f_total_savings_currency);
                $("#lblreduction_of").html(savings.reduction_of);
                $("#lbli_power_savings").html(savings.i_power_savings);
                $("#lbli_carbon_footprint_legacy").html(savings.i_carbon_footprint_legacy);
                $("#lbli_carbon_footprint_savings").html(savings.i_carbon_footprint_savings);
            })
        }
	});
});