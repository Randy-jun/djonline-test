//sessionstorage function packae
import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';

const api='http://127.0.0.1:9090/acct/agencies/';

var temp = {
    item_num: 7,
    result:[{"id":"1","name":"pearl","remark":"pearl"},
            {"id":"2","name":"pear2","remark":"pear2"},
            {"id":"3","name":"pear3","remark":"pear3"},
            {"id":"4","name":"pear4","remark":"pear4"},
            {"id":"5","name":"pear5","remark":"pear5"},
            {"id":"6","name":"pear6","remark":"pear6"},
            {"id":"7","name":"pear7","remark":"pear7"},]
}

var group = {
    get : function(){
        var params = new URLSearchParams();
        params.append("userID",Sstorage.get('userID'));
        params.append("tokeID",Sstorage.get('localAgencyFk'));
        params.append("local_agency_fk",Sstorage.get('tokenID'));

        params.append("req_method","GET");

        return new Promise((resolve, reject) => {
            temp.result.forEach(element => {
                element.isSet = false;
            });
            resolve(temp) ;
            // Axios.post(api, params).then((response) => {
            //     console.log(response);
            //     response.data.result.forEach(element => {
            //         this.$set(element, 'isSet', false);
            //     });
            //     resolve(response.data) ;
            // }).catch((error) => {
            //     // console.log(error);
            //     reject(error);
            // })
        })
    },
    update : function(value){
        var params = new URLSearchParams();
        params.append("userID",Sstorage.get('userID'));
        params.append("tokeID",Sstorage.get('localAgencyFk'));
        params.append("local_agency_fk",Sstorage.get('tokenID'));

        params.append("req_method","UPDATE");

        params.append("pk", value.id);
        params.append("name", value.name);
        params.append("remark", value.remark);

        return new Promise((resolve, reject) => {
            let tempData = {
                id:value.id,
                name: value.name,
                remark: value.remark,
            }
            tempData.isSet = false;
            resolve(tempData);
        })
        // return new Promise((resolve, reject) => {
        //     Axios.post(api, params).then((response) => {
        //         if(response.data.status_flag){
        //             // console.log(response);
        //             let tempData = response.data.result;
        //             console.log(tempData);
        //             tempData.isSet = false;

        //             resolve(tempData) ;
        //         }
        //     }).catch((error) => {
        //         // console.log(error);
        //         reject(error);
        //     })
        // })
    },
    insert : function(value){
        var params = new URLSearchParams();
        params.append("userID",Sstorage.get('userID'));
        params.append("tokeID",Sstorage.get('localAgencyFk'));
        params.append("local_agency_fk",Sstorage.get('tokenID'));

        params.append("req_method","UPDATE");

        params.append("name", value.name);
        params.append("remark", value.remark);

        return new Promise((resolve, reject) => {
            let tempData = {
                id:456,
                name: value.name,
                remark: value.remark,
            }
            tempData.isSet = false;
            resolve(tempData);
        })
        // return new Promise((resolve, reject) => {
        //     Axios.post(api, params).then((response) => {
        //         if(response.data.status_flag){
        //             // console.log(response);
        //             let tempData = response.data.result;
        //             console.log(tempData);
        //             tempData.isSet = false;

        //             resolve(tempData) ;
        //         }
        //     }).catch((error) => {
        //         // console.log(error);
        //         reject(error);
        //     })
        // })
    },
    delete : function(value){
        var params = new URLSearchParams();
        params.append("userID",Sstorage.get('userID'));
        params.append("tokeID",Sstorage.get('localAgencyFk'));
        params.append("local_agency_fk",Sstorage.get('tokenID'));

        params.append("req_method","DELETE");
        params.append("pk", value.id);

        return new Promise((resolve, reject) => {
            resolve(1);
        })
        // return new Promise((resolve, reject) => {
        //     Axios.post(api, params).then((response) => {
        //         if(response.data.status_flag){
        //             // console.log(response);

        //             resolve(tempData) ;
        //         }
        //     }).catch((error) => {
        //         // console.log(error);
        //         reject(error);
        //     })
        // })
    }
}

export default group;