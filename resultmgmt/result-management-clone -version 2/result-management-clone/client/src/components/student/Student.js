import React, { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import axios from "axios";

import Sidebar from "./Sidebar";


function Student() {
    const navigate = useNavigate();
    const { state } = useLocation()
    const { username } = state;
    const [data, setData] = useState([]);
    const [max, setMax] = useState(0);

    useEffect(() => {
        var max1 = 0;
        data.map(data => {
            max1 = Math.max(max1, data.sem);
            // console.log(max1);
        });
        console.log(max1);
        setMax(max1);
        // console.log(sem);
    }, [data]);

    useEffect(() => {
        console.log("max");
        console.log(max);
    }, [max]);

    function getData() {
        axios.post("/getresult")
            .then(res => {
                if (res.data.message === "success") {
                    console.log(res.data.result);
                    setData(res.data.result);
                }
                else {
                    alert(res.data.message);
                }
            });
    }


    return (
        // <div>
        //     <div>
        //         <h2>username: {username}</h2>
        //         <button onClick={getData}>Show result</button>
        //     </div>
        //     {data.map((semResult, i) => {
        //         return (
        //             <div>
        //                 Semister: {semResult.sem}
        //                 {semResult.total.map((marks, i) => {
        //                     return (
        //                         <div>
        //                             {marks.subject}: {marks.marks}
        //                         </div>
        //                     )
        //                 })}
        //             </div>
        //         );
        //     })}
        // </div>
        <>
            <div style={{ position: "absolute", textAlign: "", marginLeft: "10%" }}>

                <div class="text-center p-5">

                    <div  >
                        <p className="m-3">Welcome to Student DashBoard</p>
                        <h5>username: {username}</h5>
                    </div>

                    <button type="button" class="btn btn-primary m-2" onClick={getData} >Show Result</button>
                    {/* <button type="button" class="btn btn-warning text-white m-2" onClick={() => navigate("/insert-mark")} >Insert Mark</button> */}
                    {/* <button type="button" class="btn btn-danger  m-2 " onClick={() => navigate("/insert-mark")}>student login</button> */}


                </div>

                {/* {data.map((semResult, i) => {
                    
                })} */}

                {/* <div>
                    {data.map((semResult, i) => {
                        return (
                            <div>
                                Semister: {semResult.sem}
                                {semResult.total.map((marks, i) => {
                                    return (
                                        <div>
                                            {marks.subject}: {marks.marks}
                                        </div>
                                    )
                                })}
                            </div>
                        );
                    })}
                </div> */}

                <div>
                    {data.map((semResult, i) => {
                        return (<div>
                                            <table class="table table-bordered">
                                                <thead>
                                                    <tr>
                                                        <th scope="col">Max Marks</th>
                                                        <th scope="col">Sem</th>
                                                        <th scope="col">Course Name</th>
                                                        <th scope="col">Mark Obtain</th>
                                                        <th scope="col">Result</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    {/* {semResult.map((marks, i) => {
                                                        return ( */}
                                                            <tr>
                                                                <td>100</td>
                                                                <td>{semResult.sem}</td>
                                                                <td>{semResult.subject}</td>
                                                                <td>{semResult.marks}</td>
                                                                {(semResult.marks>=40)? <td>Pass</td> : <td>fail</td>}
                                                            </tr>
{/*                                                         
                                                        )
                                                    })} */}
                                                </tbody>
                                            </table>
                                        </div>
                        );
                    })}
                </div>












            </div>

            <div style={{ position: 'fixed' }}>
                <Sidebar />
            </div>
        </>


    )
}

export default Student;

