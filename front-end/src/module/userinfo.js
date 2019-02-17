//sessionstorage function packae
import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';

const api='http://127.0.0.1:9090/login/';
//======================================
var user = {
    'user0' : {
        uuuid : '0000',
        uname : 'user0',
        upassword : 'passwd',
        unickname : '系统管理员',
        ulevel : 0,
        ulevelname : '系统管理员',
        umark : '系统拥有者，权限最大。',
        guuid : '000',
        ustatusid : '0',
        ustatusname : '正常',
    },
    'user1' : {
        uuuid : '0001',
        uname : 'user1',
        upassword : 'passwd',
        unickname : '系统职员',
        ulevel : 1,
        ulevelname : '系统职员',
        umark : '系统拥有公司职员。',
        guuid : '000',
        ustatusid : '0',
        ustatusname : '正常',
    },
    'user2' : {
        uuuid : '0002',
        uname : 'user2',
        upassword : 'passwd',
        unickname : '公司管理员',
        ulevel : 2,
        ulevelname : '公司管理员',
        umark : '公司管理者，公司内权限最大。',
        guuid : '001',
        ustatusid : '0',
        ustatusname : '正常',
    },
    'user3' : {
        uuuid : '0003',
        uname : 'user3',
        upassword : 'passwd',
        unickname : '公司职员',
        ulevel : 3,
        ulevelname : '公司职员',
        umark : '公司职员，主要负责订单新增。',
        guuid : '001',
        ustatusid : '0',
        ustatusname : '正常',
    },
}
//======================================

var userInfo = {
    check : function(userInfo){
        var params = new URLSearchParams();
        params.append("username",userInfo.userName);
        params.append("password",userInfo.passWord); 

        return new Promise((resolve, reject) => {
            //===================================
            let tempData = user[String(userInfo.userName)];
            console.log(tempData);
            Sstorage.set('nickName', tempData.unickname);
            Sstorage.set('userID', tempData.uuuid);
            Sstorage.set('userLevel', tempData.ulevel);
            
            Sstorage.set('localName', tempData.guuid);
            Sstorage.set('localAgencyFk', tempData.guuid);
            
            Sstorage.set('tokenID', 'response.data.tokenID');
            resolve(tempData);
            //===================================
            // Axios.post(api, params).then((response) => {
            //     console.log(response);
            //     if(response.data.isLogin){
            //         console.log(response);
            //         Sstorage.set('nickName', response.data.NickName);
            //         Sstorage.set('userID', response.data.userID);
                    
            //         Sstorage.set('localName', response.data.DJName);
            //         Sstorage.set('localAgencyFk', response.data.local_agency_fk);
                    
            //         Sstorage.set('tokenID', response.data.tokenID);

            //         resolve(response.data) ;
            //     }
            //     reject(response.data);
            // }).catch((error) => {
            //     // console.log(error);
            //     reject(error);
            // });
        });
    },
    getLevel : function(){

        return new Promise((resolve, reject) => {
            //===================================
            // let tempData = user[String(userInfo.username)];
            console.log(tempData);
            let tempData = Sstorage.get('userLevel');
            resolve(tempData);
            //===================================
            // Axios.post(api, params).then((response) => {
            //     console.log(response);
            //     if(response.data.isLogin){
            //         console.log(response);
            //         Sstorage.set('nickName', response.data.NickName);
            //         Sstorage.set('userID', response.data.userID);
                    
            //         Sstorage.set('localName', response.data.DJName);
            //         Sstorage.set('localAgencyFk', response.data.local_agency_fk);
                    
            //         Sstorage.set('tokenID', response.data.tokenID);

            //         resolve(response.data) ;
            //     }
            //     reject(response.data);
            // }).catch((error) => {
            //     // console.log(error);
            //     reject(error);
            // });
        });
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

export default userInfo;