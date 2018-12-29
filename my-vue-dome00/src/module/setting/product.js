//sessionstorage function packae
import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';

const linePrice = 'http://127.0.0.1:9090/acct/lineprices/';
const refPrice = 'http://127.0.0.1:9090/acct/refprices/';

var product = {
    get(){
        var params = new URLSearchParams();
        params.append("req_method","GET");
        params.append("userID",Sstorage.get('userID'));
        params.append("local_agency_fk",Sstorage.get('localAgencyFk'));
        params.append("tokenID",Sstorage.get('tokenID'));

        return new Promise((resolve, reject) => {
            Axios.post(linePrice, params).then((response) => {
                // console.log(response);
                resolve(response.data) ;
            }).catch((error) => {
                // console.log(error);
                reject(error);
            })
        })
    },
    getOne(key){
        var params = new URLSearchParams();
        params.append("pk",key);
        params.append("req_method","GETONE");
        params.append("userID",Sstorage.get('userID'));
        params.append("local_agency_fk",Sstorage.get('localAgencyFk'));
        params.append("tokenID",Sstorage.get('tokenID'));

        return new Promise((resolve, reject) => {
            Axios.post(linePrice, params).then((response) => {
                console.log(response,"---------");
                if(response.data.status_flag){
                    //处理请求到的数据。回写前台
                    resolve(response.data) ;
                }
            }).catch((error) => {
                // console.log(error);
                reject(error);
            })
        })
    }
}

export default product;