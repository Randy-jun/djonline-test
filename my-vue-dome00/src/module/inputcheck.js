//sessionstorage function packae
const input = /^[\s]*$/;
var inputcheck = {
    namecheck(value){
        if(input.test(value)){
            return true;
        }
        else{
            return false;
        }
    },
}

export default inputcheck;