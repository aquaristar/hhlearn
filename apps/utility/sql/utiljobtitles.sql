INSERT INTO `util_job_titles` (`id`, `short_code`, `name`, `name_possessive`, `description`, `category_id`, `patient_file_access_id`, `exposure_to_chemicals_id`, `exposure_to_BBP_id`, `exposure_to_TB_id`, `requires_license_id`, `cpr_id`, `on_call_id`, `all_occupational_exposure_id`, `some_occupational_exposure_id`, `flsa_status_id`, `is_active`)
VALUES
	(1, 'staff_accountant', 'Staff Accountant', 'Staff Accountant\'s', NULL, 1, 0, 0, 0, 0, 1, 0, 0, NULL, NULL, 1, 1),
	(2, 'accounting_clerk', 'Accounting Clerk', 'Accounting Clerk\'s', NULL, 1, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(3, 'accounting_manager', 'Accounting Manager', 'Accounting Manager\'s', NULL, 1, 1, 0, 0, 0, 1, 0, 0, NULL, NULL, 2, 1),
	(4, 'accounts_payable_clerk', 'Accounts Payable Clerk', 'Accounts Payable Clerk\'s', NULL, 1, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(5, 'administrative_assistant', 'Administrative Assistant', 'Administrative Assistant\'s', NULL, 4, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(6, 'assistant_controller', 'Assistant Controller', 'Assistant Controller\'s', NULL, 1, 1, 0, 0, 0, 1, 0, 0, NULL, NULL, 2, 1),
	(7, 'director_of_operations', 'Director of Operations', 'Director of Operations\'', NULL, 2, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(8, 'assistive_technology_practitioner', 'Assistive Technology Practitioner', 'Assistive Technology Practitioner\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(9, 'assistive_technology_technician', 'Assistive Technology Technician', 'Assistive Technology Technician\'s', NULL, 3, 1, 1, 1, 1, 0, 0, 1, NULL, NULL, 1, 1),
	(10, 'billing_specialist_I', 'Billing Specialist I', 'Billing Specialist\'s', NULL, 5, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(11, 'billing_specialist_supervisor', 'Billing Specialist Supervisor', 'Billing Specialist Supervisor\'s', NULL, 5, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(12, 'bookkeeper', 'Bookkeeper', 'Bookkeeper\'s', NULL, 1, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(13, 'accounts_receivable_clerk', 'Accounts Receivable Clerk', 'Accounts Receivable Clerk\'s', NULL, 5, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(14, 'chief_compliance_officer', 'Chief Compliance Officer', 'Chief Compliance Officer\'s', NULL, 6, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 2, 1),
	(15, 'chief_executive_officer', 'Chief Executive Officer', 'Chief Executive Officer\'s', NULL, 2, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(16, 'chief_financial_officer', 'Chief Financial Officer', 'Chief Financial Officer\'s', NULL, 1, 0, 0, 0, 0, 1, 0, 0, NULL, NULL, 2, 1),
	(17, 'chief_technical_officer', 'Chief Technical Officer', 'Chief Technical Officer\'s', NULL, 20, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(18, 'chief_operating_officer', 'Chief Operating Officer', 'Chief Operating Officer\'s', NULL, 2, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(19, 'administrative_services_supervisor', 'Administrative Services Supervisor', 'Administrative Services Supervisor\'s', NULL, 4, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(20, 'senior_controller', 'Senior Controller', 'Senior Controller\'s', NULL, 1, 0, 0, 0, 0, 1, 0, 0, NULL, NULL, 2, 1),
	(21, 'contract_administrator', 'Contract Administrator', 'Contract Administrator\'s', NULL, 11, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(22, 'collections_specialist', 'Collections Specialist', 'Collections Specialist\'s', NULL, 8, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(23, 'credit_and_collections_manager', 'Credit & Collections Manager', 'Credit & Collections Manager\'s', NULL, 8, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(24, 'customer_service_specialist_supervisor', 'Customer Service Specialist Supervisor', 'Customer Service Specialist Supervisor\'s', NULL, 9, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 2, 1),
	(25, 'customer_service_specialist_I', 'Customer Service Specialist I', 'Customer Service Specialist\'s', NULL, 9, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(26, 'customer_service_specialist_II', 'Customer Service Specialist II', 'Customer Service Specialist\'s', NULL, 9, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(27, 'delivery_driver_technician_I', 'Delivery Driver Technician I', 'Delivery Driver Technician\'s', NULL, 10, 1, 1, 1, 1, 0, 0, 1, NULL, NULL, 1, 1),
	(28, 'delivery_driver_technician_II', 'Delivery Driver Technician II', 'Delivery Driver Technician\'s', NULL, 10, 1, 1, 1, 1, 1, 0, 1, NULL, NULL, 1, 1),
	(29, 'bereavement_coordinator', 'Bereavement Coordinator', 'Bereavement Coordinator\'s', NULL, 22, 1, 0, 0, 1, 0, 0, 1, NULL, NULL, 2, 1),
	(30, 'facilities_manager', 'Facilities Manager', 'Facilities Manager\'s', NULL, 16, 0, 1, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(31, 'account_executive', 'Account Executive', 'Account Executive\'s', NULL, 11, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(32, 'inventory_control_supervisor', 'Inventory Control Supervisor', 'Inventory Control Supervisor\'s', NULL, 7, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(33, 'inventory_control_specialist', 'Inventory Control Specialist', 'Inventory Control Specialist\'s', NULL, 7, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(34, 'licensed_vocation_nurse', 'Licensed Vocation Nurse', 'Licensed Vocation Nurse\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(35, 'registered_nurse', 'Registered Nurse', 'Registered Nurse\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(36, 'licensed_practical_nurse', 'Licensed Practical Nurse', 'Licensed Practical Nurse\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(37, 'nurse_practitioner', 'Nurse Practitioner', 'Nurse Practitioner\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(38, 'nurse_assistant', 'Nurse Assistant', 'Nurse Assistant\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(39, 'office_manager', 'Office Manager', 'Office Manager\'s', NULL, 2, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 2, 1),
	(40, 'orthotic_technician', 'Orthotic Technician', 'Orthotic Technician\'s', NULL, 3, 1, 1, 1, 1, 0, 0, 1, NULL, NULL, 1, 1),
	(41, 'certified_orthotist', 'Certified Orthotist', 'Certified Orthotist\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(42, 'payroll_and_timekeeping_clerk', 'Payroll and Timekeeping Clerk', 'Payroll and Timekeeping Clerk\'s', NULL, 14, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(43, 'payroll_manager', 'Payroll Manager', 'Payroll Manager\'s', NULL, 14, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(44, 'pharmacist', 'Pharmacist', 'Pharmacist\'s', NULL, 15, 1, 1, 1, 1, 1, 0, 1, NULL, NULL, 1, 1),
	(45, 'pharmacy_assistant', 'Pharmacy Assistant', 'Pharmacy Assistant\'s', NULL, 15, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(46, 'pharmacy_manager', 'Pharmacy Manager', 'Pharmacy Manager\'s', NULL, 15, 1, 1, 1, 1, 1, 0, 0, NULL, NULL, 2, 1),
	(47, 'pharmacy_technician', 'Pharmacy Technician', 'Pharmacy Technician\'s', NULL, 15, 1, 1, 1, 1, 1, 0, 1, NULL, NULL, 1, 1),
	(48, 'prosthetic_technician', 'Prosthetic Technician', 'Prosthetic Technician\'s', NULL, 3, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(49, 'certified_prosthetist', 'Certified Prosthetist', 'Certified Prosthetist\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(50, 'purchasing_assistant', 'Purchasing Assistant', 'Purchasing Assistant\'s', NULL, 7, 0, 1, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(51, 'purchasing_manager', 'Purchasing Manager', 'Purchasing Manager\'s', NULL, 7, 0, 1, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(52, 'finance_director', 'Finance Director', 'Finance Director\'s', NULL, 1, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(53, 'medical_records Clerk', 'Medical Records Clerk', 'Medical Records Clerk\'s', NULL, 4, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(54, 'medical_records Manager', 'Medical Records Manager', 'Medical Records Manager\'s', NULL, 4, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(55, 'regional_manager', 'Regional Manager', 'Regional Manager\'s', NULL, 2, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 2, 1),
	(56, 'registered_respiratory_therapist', 'Registered Respiratory Therapist', 'Registered Respiratory Therapist\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(57, 'safety_officer', 'Safety Officer', 'Safety Officer\'s', NULL, 16, 0, 1, 1, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(58, 'accounts_receivable_manager', 'Accounts Receivable Manager', 'Accounts Receivable Manager\'s', NULL, 5, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(59, 'sales_representative', 'Sales Representative', 'Sales Representative\'s', NULL, 11, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(60, 'secretary', 'Secretary', 'Secretary\'s', NULL, 4, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(61, 'shipping_and_receiving_clerk', 'Shipping & Receiving Clerk', 'Shipping & Receiving Clerk\'s', NULL, 7, 0, 1, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(62, 'shipping_and_receiving_supervisor', 'Shipping & Receiving Supervisor', 'Shipping & Receiving Supervisor\'s', NULL, 7, 0, 1, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(63, 'general_manager', 'General Manager', 'General Manager\'s', NULL, 11, 1, 1, 1, 1, 0, 0, 1, NULL, NULL, 2, 1),
	(64, 'hme_retail_location_manager', 'HME Retail Location Manager', 'HME Retail Location Manager\'s', NULL, 2, 1, 1, 1, 1, 0, 0, 1, NULL, NULL, 2, 1),
	(65, 'case_manager', 'Case Manager', 'Case Manager\'s', NULL, 3, 1, 0, 0, 1, 1, 0, 0, NULL, NULL, 1, 1),
	(66, 'certified_respiratory_Therapist', 'Certified Respiratory Therapist', 'Certified Respiratory Therapist\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(67, 'executive_director', 'Executive Director', 'Executive Director\'s', NULL, 2, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(68, 'data_entry_technician', 'Data Entry Technician', 'Data Entry Technician\'s', NULL, 4, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(69, 'delivery_driver_supervisor', 'Delivery Driver Supervisor', 'Delivery Driver Supervisor\'s', NULL, 10, 1, 1, 1, 1, 1, 0, 1, NULL, NULL, 2, 1),
	(70, 'human_resources_director', 'Human Resources Director', 'Human Resources Director\'s', NULL, 13, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(71, 'equipment_cleaning_technician', 'Equipment Cleaning Technician', 'Equipment Cleaning Technician\'s', NULL, 10, 0, 1, 1, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(72, 'equipment_repair_technician', 'Equipment Repair Technician', 'Equipment Repair Technician\'s', NULL, 12, 0, 1, 1, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(73, 'respiratory_therapy_manager', 'Respiratory Therapy Manager', 'Respiratory Therapy Manager\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 2, 1),
	(74, 'rehabilitation_processing_assistant', 'Rehabilitation Processing Assistant', 'Rehabilitation Processing Assistant\'s', NULL, 3, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(75, 'education_director', 'Education Director', 'Education Director\'s', NULL, 17, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(76, 'billing_specialist_II', 'Billing Specialist II', 'Billing Specialist\'s', NULL, 5, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(77, 'privacy_officer', 'Privacy Officer', 'Privacy Officer\'s', NULL, 6, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(78, 'quality_assurance_director', 'Quality Assurance Director', 'Quality Assurance Director\'s', NULL, 18, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(79, 'quality_assurance_specialist', 'Quality Assurance Specialist', 'Quality Assurance Specialist\'s', NULL, 18, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(80, 'clinical_director', 'Clinical Director', 'Clinical Director\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 2, 1),
	(81, 'intake_coordinator', 'Intake Coordinator', 'Intake Coordinator\'s', NULL, 9, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(82, 'compliance_specialist', 'Compliance Specialist', 'Compliance Specialist\'s', NULL, 6, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(83, 'human_resources_assistant', 'Human Resources Assistant', 'Human Resources Assistant\'s', NULL, 13, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(84, 'cashier', 'Cashier', 'Cashier\'s', NULL, 19, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(85, 'cashier_manager', 'Cashier Manager', 'Cashier Manager\'s', NULL, 19, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 2, 1),
	(86, 'polysomnographic_technologist', 'Polysomnographic Technologist', 'Polysomnographic Technologist\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 0, NULL, NULL, 1, 1),
	(87, 'polysomnographic_technician', 'Polysomnographic Technician', 'Polysomnographic Technician\'s', NULL, 3, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(88, 'certified_mastectomy_fitter', 'Certified Mastectomy Fitter', 'Certified Mastectomy Fitter\'s', NULL, 3, 1, 1, 1, 1, 1, 0, 0, NULL, NULL, 1, 1),
	(89, 'medical_director', 'Medical Director', 'Medical Director\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 2, 1),
	(90, 'registered_dietician', 'Registered Dietician', 'Registered Dietician\'s', NULL, 3, 1, 0, 1, 1, 1, 0, 0, NULL, NULL, 1, 1),
	(91, 'diabetes_educator', 'Diabetes Educator', 'Diabetes Educator\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 0, NULL, NULL, 1, 1),
	(92, 'certified_pedorthist', 'Certified Pedorthist', 'Certified Pedorthist\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 0, NULL, NULL, 1, 1),
	(93, 'physical_therapist', 'Physical Therapist', 'Physical Therapist\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(94, 'physical_therapy_technician', 'Physical Therapy Technician', 'Physical Therapy Technician\'s', NULL, 15, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(95, 'occupational_therapist', 'Occupational Therapist', 'Occupational Therapist\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 0, NULL, NULL, 1, 1),
	(96, 'occupational_therapy_technician', 'Occupational Therapy Technician', 'Occupational Therapy Technician\'s', NULL, 3, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(97, 'enterostomal_therapist', 'Enterostomal Therapist', 'Enterostomal Therapist\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(98, 'certified_wound_care_nurse', 'Certified Wound Care Nurse', 'Certified Wound Care Nurse\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(99, 'home_health_aide', 'Home Health Aide', 'Home Health Aide\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(100, 'certified_nursing_assistant', 'Certified Nursing Assistant', 'Certified Nursing Assistant\'s', NULL, 3, 1, 1, 1, 1, 1, 0, 1, NULL, NULL, 1, 1),
	(101, 'clinical_manager, RN', 'Clinical Manager, RN', 'Clinical Manager\'s', NULL, 3, 1, 1, 1, 1, 1, 0, 1, NULL, NULL, 2, 1),
	(102, 'mental_health, RN', 'Mental Health, RN', 'Mental Health Nurse\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(103, 'accounts_payable_manager', 'Accounts Payable Manager', 'Accounts Payable Manager\'s', NULL, 1, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(104, 'security_officer', 'Security Officer', 'Security Officer\'s', NULL, 6, 1, 0, 0, 0, 0, 0, 0, NULL, NULL, 1, 1),
	(105, 'area_manager', 'Area Manager', 'Area Manager\'s', NULL, 2, 1, 1, 1, 1, 0, 0, 1, NULL, NULL, 2, 1),
	(106, 'medical_assistant', 'Medical Assistant', 'Medical Assistant\'s', NULL, 3, 1, 1, 1, 1, 0, 1, 1, NULL, NULL, 1, 1),
	(107, 'community_relations Director', 'Community Relations Director', 'Community Relations Director\'s', NULL, 11, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, 2, 1),
	(108, 'discharge_planner', 'Discharge Planner', 'Discharge Planner\'s', NULL, 3, 1, 0, 1, 1, 1, 0, 0, NULL, NULL, 1, 1),
	(109, 'homemaker', 'Homemaker', 'Homemaker\'s', NULL, 21, 1, 1, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(110, 'hospice_chaplain', 'Hospice Chaplain', 'Hospice Chaplain\'s', NULL, 22, 1, 0, 1, 1, 1, 0, 1, NULL, NULL, 1, 1),
	(111, 'infusion_therapy Coordinator', 'Infusion Therapy Coordinator', 'Infusion Therapy Coordinator\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 2, 1),
	(112, 'medical_social_worker', 'Medical Social Worker', 'Medical Social Worker\'s', NULL, 3, 1, 1, 1, 1, 1, 0, 1, NULL, NULL, 1, 1),
	(113, 'patient_care_coordinator', 'Patient Care Coordinator', 'Patient Care Coordinator\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 2, 1),
	(114, 'social_services_supervisor', 'Social Services Supervisor', 'Social Services Supervisor\'s', NULL, 3, 1, 0, 0, 0, 1, 0, 1, NULL, NULL, 2, 1),
	(115, 'speech_therapist', 'Speech Therapist', 'Speech Therapist\'s', NULL, 3, 1, 0, 1, 1, 1, 1, 0, NULL, NULL, 1, 1),
	(116, 'volunteer', 'Volunteer', 'Volunteer\'s', NULL, 21, 0, 0, 1, 1, 0, 0, 0, NULL, NULL, 1, 1),
	(117, 'volunteer_coordinator', 'Volunteer Coordinator', 'Volunteer Coordinator\'s', NULL, 21, 0, 0, 1, 1, 0, 0, 0, NULL, NULL, 2, 1),
	(118, 'equipment_repair_manager', 'Equipment Repair Manager', 'Equipment Repair Manager\'s', NULL, 12, 0, 1, 1, 1, 0, 0, 1, NULL, NULL, 2, 1),
	(119, 'infection_control_nurse', 'Infection Control Nurse', 'Infection Control Nurse\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1),
	(120, 'infection_prevention_director', 'Infection Prevention Director', 'Infection Prevention Director\'s', NULL, 3, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 2, 1),
	(121, 'emergency_preparedness_officer', 'Emergency Preparedness Officer', 'Emergency Preparedness Officer\'s', NULL, 16, 0, 1, 1, 1, 0, 0, 1, NULL, NULL, 1, 1);