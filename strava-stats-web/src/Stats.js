import React, { useEffect } from 'react';
import { AnimatedCounter } from  'react-animated-counter';

const baseUrl = 'https://strava-stats.azurewebsites.net/api/strava-stats';

export const fetchStats = async () => {
    
}

export const Stats = () => {
    const [ride, setRide] = React.useState(0);
    const [run, setRun] = React.useState(0);

    const getData = () => fetch(baseUrl)
        .then(data => data.json())
        .then(json => {
        setRide(json.Ride);
        setRun(json.Run)
        }
    )
    .catch(function(error) {
        console.log(error)
    });

    getData();

    useEffect(() => {
        const intervalId = setInterval(() => {
            fetch(baseUrl)
              .then(data => data.json())
              .then(json => {
                setRide(json.Ride);
                setRun(json.Run)
              }
             )
             .catch(function(error) {
                console.log(error)
             })
        }, 30000);
        return () => clearInterval(intervalId);
    }, []);
    
    return (
        <div>
            <h1 className="h1">Ride</h1>
            <AnimatedCounter
                includeDecimals={true}
                value={ride}
                color='black'
                fontSize='40px'
            />
            <h1>Run</h1>
            <AnimatedCounter
                includeDecimals={true}
                value={run}
                color='black'
                fontSize='40px'
            />
        </div>
    );
}
