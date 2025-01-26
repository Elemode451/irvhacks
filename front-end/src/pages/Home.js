import React from 'react';
import DoctorButton from '../Components/DoctorButton';

const Home = () => {
    return (
        <div className="bg-[#121212] min-h-screen">
            <div className="h-[calc(100vh-60px)]">
                <img src="/Landing_Page.png" alt="Full Screen Image" className="w-full h-full object-cover" />
            </div>
            <div className="absolute top-[625px] left-[225px] transform -translate-x-1/2 -translate-y-1/2">
                <DoctorButton />
            </div>
        </div>

    );
  };
  

export default Home;