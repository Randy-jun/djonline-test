//sessionstorage function packae

var sstorage = {
    set(key, value){
        window.sessionStorage.setItem(key, JSON.stringify(value));
    },
    get(key){
        return JSON.parse(window.sessionStorage.getItem(key));
    },
    remove(key){
        window.sessionStorage.removeItem(key);
    }
}

export default sstorage;