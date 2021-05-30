import React from 'react';
import { Link } from 'react-router-dom';
import styled from "styled-components";

const NotFoundHeader = styled.div`
    color:white;
    text-align:center;
    margin: 15% 0 5% 0;
    font-size:2rem;
`

const NotFoundMessage = styled.div`
    width:100%;
    margin: 5% 0 10% 0;
    font-size:2rem;
    text-align:center;
    color : white;
`

const LinkWrapper = styled.div`
    text-align:center;

`


const HomeLink = styled(Link)`
   
    text-align:center;
    text-decoration:none;
    color:#00e6b0;
    font-size:2rem;
 

`

function PageNotFound() {
    // let [underline, setUnderline] = useState({left:"0%"})

    return (
        <>

        <NotFoundHeader>
            Page Not Found 404
        </NotFoundHeader>
            <NotFoundMessage>
            요청하신 페이지를 찾을 수 없습니다. 
            
            </NotFoundMessage>
            < LinkWrapper >
            <HomeLink to="/">홈으로</HomeLink>
            </LinkWrapper>

                
        </>
    )
}
export default PageNotFound;