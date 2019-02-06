//sessionstorage function packae
import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';

const api='http://127.0.0.1:9090/login/';


var userinfo = {
    check : function(userinfo){
        var params = new URLSearchParams();
        params.append("username",userinfo.username);
        params.append("password",userinfo.password); 

        return new Promise((resolve, reject) => {
            Axios.post(api, params).then((response) => {
                console.log(response);
                if(response.data.isLogin){
                    console.log(response);
                    Sstorage.set('nickName', response.data.NickName);
                    Sstorage.set('userID', response.data.userID);
                    
                    Sstorage.set('localName', response.data.DJName);
                    Sstorage.set('localAgencyFk', response.data.local_agency_fk);
                    
                    Sstorage.set('tokenID', response.data.tokenID);

                    resolve(response.data) ;
                }
                reject(response.data);
            }).catch((error) => {
                // console.log(error);
                reject(error);
            })
        })
    },
    // getOne(key){
    //     var params = new URLSearchParams();
    //     params.append("pk",key);
    //     params.append("req_method","GETONE");
    //     params.append("userID",Sstorage.get('userID'));
    //     params.append("local_agency_fk",Sstorage.get('localAgencyFk'));
    //     params.append("tokenID",Sstorage.get('tokenID'));

    //     return new Promise((resolve, reject) => {
    //         Axios.post(linePrice, params).then((response) => {
    //             console.log(response,"---------");
    //             if(response.data.status_flag){
    //                 //处理请求到的数据。回写前台
    //                 resolve(response.data) ;
    //             }
    //         }).catch((error) => {
    //             // console.log(error);
    //             reject(error);
    //         })
    //     })
    // }
}

export default userinfo;