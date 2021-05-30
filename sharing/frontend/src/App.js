import React, { useState } from 'react';
import './App.css';

import Header from './components/Header';
import LoginModal from './components/auth/LoginModal';
import PageNotFound from './components/exception/PageNotFound';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";


function App() {
  let [modal, setModal] = useState(false);
  return (
    <>

      <Router>
        <Switch>


          {/* 정확한 경로를 표시해주기 위해 ( 모든 경로에는 '/' 가 들어 있기 때문 ) 해당 경로로 정확히 들어가야 들어갈 수 있는 exact path 추가 */}
          {/* Switch 사용. 첫번째로 매칭되는 값이 모두 없으면 pagenotfound 로 가기. */}

          <Route exact path="/" component={Header} modal={modal} />
          <Route path="/login" component={LoginModal} setModal={setModal} />
          <Route component={PageNotFound} />



        </Switch>



      </Router>

    </>
  );
}

export default App;