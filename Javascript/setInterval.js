import React from 'react';
import { useEffect , useState } from 'react'

function App() {
const [secound,setSecounds]=useState(0);

useEffect(()=>{
  const timer=setInterval(()=>{
    setSecounds((prevSecound)=>prevSecound+1)
  },1000);
  return()=>{
    clearInterval(timer);
  }
},[]);
return(
  <div>

  <p>{secound}</p>
  
  </div>
)

}

export default App
