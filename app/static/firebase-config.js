// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAH3Qi0yhz6VL3G277a5UmlZtQameVCmwI",
  authDomain: "fs-task-1.firebaseapp.com",
  projectId: "fs-task-1",
  storageBucket: "fs-task-1.firebasestorage.app",
  messagingSenderId: "925819325440",
  appId: "1:925819325440:web:44902fab6c6b649a47dce5",
  measurementId: "G-685GBD1KEF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);