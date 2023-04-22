import React, { useEffect, useState } from 'react';
// import {
//   BrowserRouter,
//   Routes,
//   Route
// } from "react-router-dom";
import Hero from "./Hero";

function App() {

  return (
    // <BrowserRouter>
    //   <Routes>
    //     <Route exact path="/" element={<Hero/>}/>
    //   </Routes>
    // </BrowserRouter>
    <div>
      <Hero />
    </div>
  );
}

export default App;
