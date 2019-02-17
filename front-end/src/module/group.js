//sessionstorage function packae
import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';
import { groupList, groupAdd } from '@/api/api'

//=========================================================
var groupData = {
    item_num : 7,
    data : [{id:1,name:"pearl",remark:"remark_pearl",statuscode:0,statusflag:"正常",},
            {id:2,name:"pear2",remark:"remark_pear2",statuscode:0,statusflag:"正常",},
            {id:3,name:"pear3",remark:"remark_pear3",statuscode:0,statusflag:"正常",},
            {id:4,name:"pear4",remark:"remark_pear4",statuscode:0,statusflag:"正常",},
            {id:5,name:"pear5",remark:"remark_pear5",statuscode:0,statusflag:"正常",},
            {id:6,name:"pear6",remark:"remark_pear6",statuscode:0,statusflag:"正常",},
            {id:7,name:"pear7",remark:"remark_pear7",statuscode:0,statusflag:"正常",},],
    }
//=========================================================

var group = {
    get : function(){
//=========================================================        
        return new Promise((resolve, reject) => {
            groupList().then((response) => {
                // console.log(response);
                resolve(response.data) ;
            }).catch((error) => {
                console.log(error);
                reject(error);
            });
        }).catch((error) => {
            console.log(error);
            reject(error);
        });
    },
    update : function(value){
        return new Promise((resolve, reject) => {
            groupUpdate({
                org_id:value.id,
                org_name: value.name,
                org_remark:value.remark,
                org_statuscode:value.statuscode,
            }).then((response) => {
                console.log(response);
                resolve(response.data) ;
            }).catch((error) => {
                console.log(error);
                reject(error);
            });
        }).catch((error) => {
            // console.log(error);
            reject(error);
        });
    },
    insert : function(value){
        return new Promise((resolve, reject) => {
            groupAdd({
                org_name: value.name,
                org_remark:value.remark,
                org_is_active:value.statuscode,
            }).then((response) => {
                console.log(response);
                resolve(response.data) ;
            }).catch((error) => {
                console.log(error);
                reject(error);
            });
        }).catch((error) => {
            // console.log(error);
            reject(error);
        });
    },
    delete : function(value){
        var params = new URLSearchParams();
        params.append("userID",Sstorage.get('userID'));
        params.append("tokeID",Sstorage.get('localAgencyFk'));
        params.append("local_agency_fk",Sstorage.get('tokenID'));

        params.append("req_method","DELETE");
        params.append("pk", value.id);

        return new Promise((resolve, reject) => {
            resolve(true);
        }).catch((errot) => {
            reject(error);
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