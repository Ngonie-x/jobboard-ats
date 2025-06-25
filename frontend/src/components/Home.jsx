import { useEffect, useState } from "react";
import { fetchJobs } from "../api/axios";
import JobList from "./JobList";



export default function Home(){
    const [jobs, setJobs] = useState([]);
    const [isLoadingJobs, setIsLoadingJobs] = useState(false);

    useEffect(()=>{
        const loadJobs = async ()=>{
            setIsLoadingJobs(true);

            try{
                const response = await fetchJobs();
                setJobs(response);
            }catch(error){
                console.error("Failed to fetch jobs:", error);
            }finally{
                setIsLoadingJobs(false);
            }
        }

        loadJobs();


        
    }, [])

    return (
        <>
            <JobList jobs={jobs} isLoading={isLoadingJobs}/>
        </>
    )
}