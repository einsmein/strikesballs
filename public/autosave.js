var AutoSave = (function(){

	var timer = null;

	function getEditor(){

                elems = ace.edit("editor")
                return elems;
	}


	function save(){

		var editor = getEditor(); 
                if (editor) {
		    localStorage.setItem("py_src", editor.session.getValue())
                }

	}

	return { 

		start: function(){

			if (timer != null){
				clearInterval(timer);
				timer = null;
			}

			timer = setInterval(save, 5000);


		},

		stop: function(){

			if (timer){ 
				clearInterval(timer);
				timer = null;
			}

		}
	}

}())
