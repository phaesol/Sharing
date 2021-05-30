import React from 'react';
import { Link } from 'react-router-dom';
import styled from "styled-components";

const HeaderContainer = styled.div`
  width:100%;
  height:100px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  margin:5% 0;

`

const Logo = styled.div`
  font-size:2rem;
 
  margin-left:5%


`

const HomeLink = styled(Link)`
  text-decoration:none;
  color:#00e6b0;
 

`


const Login = styled.div`
  width:10%;

`

const LoginLink = styled(Link)`
 
  text-decoration:none;
  background-color:#00e6b0;
  color:#00131b;
  padding:12% 20%;
  margin-right:5%;
  border-radius:5px;
  font-size:1rem;

`

const NavContainer = styled.div`
    width : 100%;
    display:flex;
`

const StyledLink = styled(Link)`
    text-decoration:none;
    color:white;
`

const Home = styled.div`
    color : white;
    font-size:1.6rem;
    width:20%;
    text-align:center;
   
`

const NavBar = styled.div`
    font-size : 1.6rem;
  
`


function Header() {

  return (
    <>
      < HeaderContainer>
        <Logo>
          <HomeLink className="header-logo" to="/">Sharing</HomeLink>
        </Logo>
        <Login>
          <LoginLink to="/login">로그인</LoginLink>
        </Login>
      </HeaderContainer>

      <NavContainer>


        <Home>
          <StyledLink className="navi-" to="/">
            🤞홈
    </StyledLink>
        </Home>


        <NavBar>
          <StyledLink className="navi-" to="/">
            🤷‍♂️카테고리 추가 예정
     </StyledLink>
        </NavBar>

        <div className="navi-underline"></div>

      </NavContainer>
    </>
  )
}

export default Header;