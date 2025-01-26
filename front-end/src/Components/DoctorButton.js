import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight } from 'lucide-react'; // For the right arrow icon

const FindDoctorButton = () => {
  return (
    <Link
      to="/search"
      className="font-bold w-[200px] flex items-center justify-center gap-2 px-6 py-3 border-[7px] border-[#4CB963] text-[#4CB963] bg-transparent font-roboto text-lg rounded-lg transition-all duration-300 hover:bg-[#4CB963] hover:text-white"
    >
      Find Doctors
      <ArrowRight className="w-5 h-5" />
    </Link>
  );
};

export default FindDoctorButton;
