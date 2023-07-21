import React, { useEffect } from 'react';
import { AnimatedCounter } from  'react-animated-counter';
import './Stats.css';
import magnolia from './img/magnolia.jpg';
import bridle from './img/bridle.jpg';
import bikeImage from './img/bike.png';
import runImage from './img/run.png';

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
            <div className='container'>
                <div className='flexBody'>
                    <div className='flexBodyItem' style={{backgroundImage: `url(${magnolia})`}}>
                        <img className='icon' src={bikeImage} alt='biker' />
                        <div className='counter'>
                            <AnimatedCounter
                                includeDecimals={true}
                                value={ride}
                                color='white'
                                fontSize='80px'
                            />
							<p>mi</p>
                        </div>
                    </div>
                    <div className='flexBodyItem' style={{backgroundImage: `url(${bridle})`}}>
                        <img className='icon' src={runImage} alt='runner' style={{paddingTop: '2em'}} />
                        <div className='counter'>
                            <AnimatedCounter
                                includeDecimals={true}
                                value={run}
                                color='white'
                                fontSize='80px'
                            />
							<p>mi</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
