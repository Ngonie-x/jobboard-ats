import JobDetail from "../components/JobDetail";
import { fetchJob } from "../api/axios";
import { useLoaderData, Await } from "react-router-dom";
import { Suspense } from "react";

export default function JobDetailPage(){
    const {job} = useLoaderData();
    return (
        <Suspense fallback={<p style={{textAlign: 'center'}}>Loading...</p>}>
            <Await resolve={job}>
                {(resolvedJob) => <JobDetail job={resolvedJob} />}
            </Await>
        </Suspense>
    )
}


export async function loader({params}){
    const id = params.id;
    return {
        job: fetchJob(id)
    }
}