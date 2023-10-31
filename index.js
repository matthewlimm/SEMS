import { initializeApp } from "firebase/app";
import {getAuth, onAuthStateChanged } from 'firebase/auth';
import {getFirestore} from 'firebase/firestore';

const firebaseApp = initializeApp({
  apiKey: "AIzaSyAT3TKqTwfpeUfICN7PaVwMmPpWRmTTvUw",
  authDomain: "engineering-be843.firebaseapp.com",
  projectId: "engineering-be843",
  storageBucket: "engineering-be843.appspot.com",
  messagingSenderId: "813909430707",
  appId: "1:813909430707:web:187ccdccf7a96c6ae3bbc6",
  measurementId: "G-X0JB8FPHQQ"
});

onAuthStateChanged(auth, user => {
    if (user != null) {
        console.log('logged in!')
    } else {
        console.log('No user')
    }


})