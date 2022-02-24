const app = new Vue({

    el: '#main',
   
    data: {

        results: "",
        responseAvailable: false,
        q : ""
    },

    methods: {

        fetchAPIData( ) { 
            this.responseAvailable = false;

            fetch(`http://127.0.0.1:5000/get/${this.q}` , {
                "method": "GET"
            })
            .then(response => { 
                if(response.ok){
                    return response.json()
                } else{
                    alert("Server returned " + response.status + " : " + response.statusText);
                }                
            })
            .then(response => {
                this.results = response['result'];
                this.responseAvailable = true;
            })
            .catch(err => {
                console.log(err);
            });
            console.log(this.result);
        }
    }

})