import React, { useEffect, useState } from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';

import hat from './assets/hat.png';
import eye from './assets/eye.png';
import moustache from './assets/moustache.png';
import mouth from './assets/mouth.png';
import { HiOutlineMicrophone } from 'react-icons/hi';
import './App.css';

function Hero() {
  const [data, setData] = useState([{}]);
  const [animateMouth, setAnimateMouth] = useState(false);

  const commands = [
    {
      command: 'reset',
      callback: ({ resetTranscript }) => resetTranscript()
    }

  ]

  const {
    transcript,
    interimTranscript,
    finalTranscript,
    resetTranscript,
    listening,
  } = useSpeechRecognition({ commands });



  useEffect(() => {

    var msg = new SpeechSynthesisUtterance();
    var voices = window.speechSynthesis.getVoices();

    msg.voice = voices[4]; 
    msg.volume = 1; // From 0 to 1
    msg.rate = 1.1; // From 0.1 to 10
    msg.pitch = 1.2; // From 0 to 2

    async function processData(finalTranscript) {
      fetch('api/client_message', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(finalTranscript)
      })
        .then(function (response) {
          console.log(response);  
          return response.json();
        })
        .then(function (myJson) {
          console.log(myJson);
          setData(myJson);

          msg.text = myJson.msg;
          window.speechSynthesis.speak(msg);
          
          //received response animate mouth
          setAnimateMouth(true);
          setTimeout(() => {
            setAnimateMouth(false);
          }, myJson.msg.length*80);
        })
  
    }

    if (finalTranscript !== '') {
      resetTranscript();
      //console.log('Got final result:', finalTranscript);

      //send message to flask server
      processData(finalTranscript);


    }
  }, [interimTranscript, finalTranscript, resetTranscript, data]);

  if (!SpeechRecognition.browserSupportsSpeechRecognition()) {
    return null
  };


  return (
    <div className="App">

      <div className='buttons'>
        <button type='button' onClick={() => SpeechRecognition.startListening({ continuous: true, language: 'en-GB' })} className='microphone'>
          <HiOutlineMicrophone />
        </button>
      </div>

      <header className="App-header">
        <div className="hero-face">
          <div className="hat">
            <img src={hat} alt="hat"></img></div>
          <div className="eyes">
            <img src={eye} alt="left-eye"></img>
            <img src={eye} alt="right-eye"></img>
          </div>
          <div className="mouth">
            <div className="moustache"><img src={moustache} alt="moustache"></img></div>
            <div className={`${animateMouth && `lip-animate`} lip`}><img src={mouth} alt="mouth"></img></div>
          </div>
        </div>
      </header>

      <div className="content-container">
        <div className="main-content">

          <div className="intro">
            Welcome back!
          </div>
          <div className="main-text">
            {(typeof data.msg !== 'undefined') && (
              data.msg
            )}</div>
          <div className="">{transcript}</div>

        </div>


        <span>
          listening:
          {' '}
          {listening ? 'on' : 'off'}
        </span>

      </div>
    </div>
  );
}

export default Hero;
