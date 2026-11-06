import React from 'react';
import { useState,useRef } from 'react'

function App() {
const newUseRef=useRef(null);

const handleClick=()=>{
  newUseRef.current.style.color="red";

};

const handleRemove=()=>{
  newUseRef.current.style.color="black";
};

return(
  <div>

  <p ref={newUseRef}
  >ok</p>
  <button onClick={handleClick}>press</button>
  <button onClick={handleRemove}>remove</button>
  
  </div>
)

}

export default App
