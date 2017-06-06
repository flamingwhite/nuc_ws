let firebase = require('firebase');
let Rx = require('rxjs/Rx');
let {curry} = require('ramda');

let app = null;
let connect = config => app = firebase.initializeApp(config);

var config = {
	apiKey: "AIzaSyDhghirxL19-LekWjgvfq4uLGXOO_zDeRo",
	authDomain: "justdemo-ac305.firebaseapp.com",
	databaseURL: "https://justdemo-ac305.firebaseio.com",
	projectId: "justdemo-ac305",
	storageBucket: "justdemo-ac305.appspot.com",
	messagingSenderId: "338492799528"
};
firebase.initializeApp(config);


// let fireStream = ref => Rx.Observable.fromEvent(ref, 'value');

let rxOn = (target, event) => Rx.Observable.create(obs => {
	target.on(event, evt => {
		obs.next(evt);
	});
});

let getRef = refOrPath => typeof refOrPath == 'string' ? firebase.database().ref(refOrPath) : refOrPath;

let fireStream = refOrPath => {
	refOrPath = getRef(refOrPath);
	return rxOn(refOrPath, 'value').map(value => value.val());
};

let fireArrayStream = refOrPath => fireStream(refOrPath).map(data => Object.entries(data).map(([_id, value]) => ({ _id, ...value })));

fireArrayStream('users/').subscribe(v => console.log(v));

let fireCreate = curry(( refOrPath, data ) => {
	let ref = getRef(refOrPath);
	let newRecord = ref.push();
	newRecord.set({...data});
});

let fireUpdate = curry((refOrPath, data) => getRef(refOrPath).set(data));

let fireRemoveById = curry((refOrPath, _id) => getRef(refOrPath).child(_id).remove());


let fireRef = refOrPath => {
	let ref = getRef(refOrPath);
	return {
		stream: () => fireStream(ref),
		arrayStream: () => fireArrayStream(ref),
		create: fireCreate(ref),
		removeById: fireRemoveById(ref)
	};
}


module.exports = {
	connect,
	firebase,
	fireRef,
	fireStream,
	fireArrayStream,
	fireUpdate,
	fireRemoveById
};
